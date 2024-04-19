class Box:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

class student:
    def __init__(self,fees):
        self.fees=fees

class Box2(Box,student):
    def __init__(self,name,rollno,marks,fees):
        self.marks=marks
        student.__init__(self,fees)
        Box.__init__(self,name,rollno)
    
class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"girish",12,23,20)

obj=Box3("2-1")
print(obj.sem)
print(obj.name)



obj2=Box2("girish",12,23,20)
print(obj2.fees)
print(obj2.roll)
print(obj2.marks)
print(obj2.name)

obj3=Box2("raj",34,453,43533)
print(obj3.name)
print(obj3.roll)
print(obj3.marks)
print(obj3.fees)