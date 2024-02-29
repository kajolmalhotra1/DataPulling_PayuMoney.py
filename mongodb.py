import pandas as pd
import pymongo

#df = pd.read_excel(r'D:\vinstore\Data-Pulling-PayUMoneyy\Students.xlsx').set_index('id')

# connect to mongodb
# connection = pymongo.MongoClient('mongodb://localhost:27017/')
# db = connection.students
# collection = db.students_list
# json_data = df.to_json(orient="records")
# print(json_data)
# mydict = {"status":0,"msg":"Merchant key is empty"}
# x = collection.insert_one(mydict)

df = pd.read_excel(r'D:\vinstore\Data-Pulling-PayUMoneyy\Students.xlsx').set_index('id')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["mycollection"]
json_data = df.to_json(orient="records")
print(json_data)
#mydict = {"status":0,"msg":"Merchant key is empty"}
# mydict = {'key': 'JPM7Fg', 'command': 'get_Transaction_Details', 'var1': '2020-10-20', 'var2': '2020-10-27', 'hash': '0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634'}
# x = mycol.insert_one(mydict)
# print(x)


