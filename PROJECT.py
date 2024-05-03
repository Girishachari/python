import datetime


class DispatchSystem:   #DispatchSystem: Defines the main class to manage dispatch records.


    def __init__(self): #This should be _init_ to be recognized as the constructor. It initializes the file_path attribute to "police_record.txt".

        self.police_records = {}
        self.file_path = "police_record.txt"

    def convert_file_to_list(self):  #Reads the contents of "police_record.txt", evaluates it as a dictionary, and returns the list of dispatch records stored in it.
        try:
            with open(self.file_path, "r") as file:
                return eval(file.read())["store"]
            
        except FileNotFoundError:
            return []  # Return empty list if file doesn't exist

    def insert_into_file(self, data_list):  #Writes the provided list of dispatch records into "police_record.txt".

        with open(self.file_path, "w") as file:
            obj = {"store": data_list}
            file.write(str(obj))

    def create_dispatch_record(self, dispatch_id, incident_type, location, caller_name, caller_number, dispatch_time):
        """ #Writes the provided list of dispatch records into "police_record.txt".

        Creates a new dispatch record with details and stores it in the file.
        """
        dispatch_data = {
            'dispatch_id': dispatch_id,
            'incident_type': incident_type,
            'location': location,
            'caller_name': caller_name,
            'caller_number': caller_number,
            'dispatch_time': dispatch_time.strftime("%Y-%m-%d %H:%M:%S"),
            'response_time': None  # Initially response time is None
        }
        curr_list = self.convert_file_to_list()
        curr_list.append(dispatch_data)
        self.insert_into_file(curr_list)
        print("Dispatch record created successfully.")

    def read_dispatch_record(self, dispatch_id):
        dispatch_id = int(dispatch_id)
        record = next((rec for rec in self.convert_file_to_list() if rec['dispatch_id'] == dispatch_id), None)

        if not record:
            print("Dispatch ID does not exist")
            return

        print("Dispatch ID:", record['dispatch_id'])
        print("Incident Type:", record['incident_type'])
        print("Location:", record['location'])
        print("Caller Information:", record['caller_number'])
        print("Dispatch Time:", record['dispatch_time'])
        print("Response Time:", record['response_time'])

    def update_dispatch_record(self, dispatch_id, incident_type, location, caller_name, caller_number, response_time):
        """
        Updates an existing dispatch record with new details and response time, and stores the changes in the file.
        """
        curr_list = self.convert_file_to_list()
        updated_record = None

        for record in curr_list:
            if record['dispatch_id'] == dispatch_id:
                if incident_type != "":
                    record['incident_type'] = incident_type
                if location != "":
                    record['location'] = location
                if caller_name != "":
                    record['caller_name'] = caller_name
                if caller_number != "":
                    record['caller_number'] = caller_number
                if response_time is not None:
                    record['response_time'] = response_time.strftime("%Y-%m-%d %H:%M:%S")
                updated_record = record
                break

        if updated_record:
            self.insert_into_file(curr_list)
            print("Dispatch record updated successfully.")
        else:
            print("Dispatch ID not found.")

    def delete_dispatch_record(self, dispatch_id):
        """
        Deletes a dispatch record and its corresponding response time, and updates the file.
        """
        curr_list = self.convert_file_to_list()
        new_list = [record for record in curr_list if record['dispatch_id'] != dispatch_id]

        if len(new_list) < len(curr_list):
            self.insert_into_file(new_list)
            print("Dispatch record deleted successfully.")
        else:
            print("Dispatch ID not found.")

    def manage_dispatches(self, dispatch_id, incident_status):
        """
        Logs the status of a dispatch based on incident ID and updates the file.
        """
        if incident_status not in ["responded", "resolved"]:
            print("Invalid incident status. Please enter 'responded' or 'resolved'.")
            return

        curr_list = self.convert_file_to_list()
        for record in curr_list:
            if record['dispatch_id'] == dispatch_id:
                if incident_status == "responded":
                    if record['response_time'] is None:
                        response_time = datetime.datetime.now()
                        record['response_time'] = response_time.strftime("%Y-%m-%d %H:%M:%S")
                        self.insert_into_file(curr_list)
                        print("Dispatch marked as responded.")
                        return
                    else:
                        print("Dispatch already responded.")
                        return
                elif incident_status == "resolved":
                    print("Dispatch marked as resolved.")
                    self.insert_into_file(curr_list)
                    return

        print("Dispatch ID not found.")

    def track_response_times(self, time_id=None):
        """
        Analyzes and displays response times.
        """
        if time_id:
            curr_list = self.convert_file_to_list()
            for record in curr_list:
                if record['dispatch_id'] == time_id and record['response_time'] is not None:
                    dispatch_time = datetime.datetime.strptime(record['dispatch_time'], "%Y-%m-%d %H:%M:%S")
                    response_time = datetime.datetime.strptime(record['response_time'], "%Y-%m-%d %H:%M:%S")
                    time_difference = response_time - dispatch_time
                    print(f"Response Time for Dispatch ID {time_id}: {time_difference}")
                    return

            print(f"Dispatch ID {time_id} not found or response time not recorded.")
        else:
            print("Response times for all dispatches:")
            curr_list = self.convert_file_to_list()
            for record in curr_list:
                if record['response_time'] is not None:
                    dispatch_time = datetime.datetime.strptime(record['dispatch_time'], "%Y-%m-%d %H:%M:%S")
                    response_time = datetime.datetime.strptime(record['response_time'], "%Y-%m-%d %H:%M:%S")
                    time_difference = response_time - dispatch_time
                    print(f"Dispatch ID {record['dispatch_id']}: {time_difference}")

# Example Usage
tracker = DispatchSystem()


while True:
    print("\n\n**")
    print("\nChoose an option:")
    print("1. Create dispatch record")
    print("2. Update dispatch record")
    print("3. Delete dispatch record")
    print("4. Manage dispatch status")
    print("5. Track response times")
    print("6. read dispatch record")
    print("7.Exit")

    choice = input("Enter your choice: ")
    print("\n\n**")

    if choice == '1':
        print("\nCreating Dispatch Record:")
        dispatch_id = int(input("Enter dispatch ID: "))
        incident_type = input("Enter incident type: ")
        location = input("Enter location: ")
        caller_name = input("Enter caller name: ")
        caller_number = input("Enter caller number: ")
        dispatch_time = datetime.datetime.now()
        tracker.create_dispatch_record(dispatch_id, incident_type, location, caller_name, caller_number, dispatch_time)
    elif choice == '2':
        print("\nUpdating Dispatch Record:")
        dispatch_id = int(input("Enter dispatch ID to update: "))
        incident_type = input("Enter new incident type (Press Enter to keep old value): ")
        location = input("Enter new location (Press Enter to keep old value): ")
        caller_name = input("Enter new caller name (Press Enter to keep oldvalue): ")
        caller_number = input("Enter new caller number (Press Enter to keep old value): ")
        response = input("Enter 'yes' if incident is responded, otherwise press Enter: ")
        if response.lower() == 'yes':
            response_time = datetime.datetime.now()
        else:
            response_time = None
        tracker.update_dispatch_record(dispatch_id, incident_type, location, caller_name, caller_number, response_time)
    elif choice == '3':
        print("\nDeleting Dispatch Record:")
        dispatch_id = int(input("Enter dispatch ID to delete: "))
        tracker.delete_dispatch_record(dispatch_id)
    elif choice == '4':
        print("\nManaging Dispatch Status:")
        dispatch_id = int(input("Enter dispatch ID: "))
        status = input("Enter 'responded' or 'resolved': ")
        tracker.manage_dispatches(dispatch_id, status)
    elif choice == '5':
        print("\nTracking Response Times:")
        dispatch_id = int(input("Enter dispatch ID to track response time: "))
        tracker.track_response_times(dispatch_id)
    elif choice == '6':
        print("dispatched details are :")
        dispatch_id=int(input("Enter dispatched ID to read: "))
        tracker.read_dispatch_record(dispatch_id)
    elif choice=='7':
        exit
    else:
        print("Invalid choice. Please try again.")
