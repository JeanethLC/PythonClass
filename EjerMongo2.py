import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["mydatabase"]

dblist = myClient.list_database_names()
if "mydatabase" in dblist:
  print("La base de datos existe.")
