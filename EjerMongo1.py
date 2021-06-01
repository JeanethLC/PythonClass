import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["mydatabase"]
mycol = mydb["customers"]
mydict = {"name":"Cristian", "address": "Av Vallcarca"}
x = mycol.insert_one(mydict)
print(x.inserted_id)
mylist = [
    {"_id": 7, "name": "uno", "address": "diruno"},
    {"_id": 8, "name": "dos", "address": "dirdos"},
    {"_id": 9, "name": "tres", "address": "dirtres"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)
