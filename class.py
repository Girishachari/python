class Card:
    def __init__(self,imageUrl,price,rating,description,deliverywithin,comments,brandName):
        self.imageUrl = imageUrl
        self.price = price
        self.rating = rating
        self.description = description
        self.deliverywithin = deliverywithin
        self.comments = comments
        self.brandName = brandName

    def printalldetails(self):
        print("product brand is : ",self.brandName)
        print("product price is : ",self.price)
        print("product rating is : ",self.rating)

    def printalldetails(self):
        print("product brand is : ",self.brandName)
        print("product price is : ",self.price)
        print("product rating is : ",self.rating)
                    
commentsforlaptop =["THIS IS GOOD ","OKAY!","NOT GOOD"]
laptop=Card("dummy-url-1",90000,4.5,"this is good performence laptop","10 days","+++","SAMSUNG")
laptop.printalldetails()