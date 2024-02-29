
import json
import pymongo
import requests

# @app.task()
def reverse_text():
    url = "https://test.payu.in/merchant/postservice?form=2"
    payload = "key=JPM7Fg&command=get_Transaction_Details&var1=2020-10-20&var2=2020-10-27&hash=0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634"
    headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }
    response = requests.request("POST", url, data =payload, headers=headers)
    data = (json.loads(response.text))
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["mycollection"]
    mycol.insert_many(data['Transaction_details'])






















