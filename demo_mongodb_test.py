import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb= myclient["mydatabase"]
mycol = mydb["email"]

mydict = {"email":"v@gmail.com"}

x=mycol.find(mydict)

print(x)
for i in x:
    print(i)