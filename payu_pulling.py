import requests
import json
from pymongo import MongoClient
from celeryapp import app

@app.task
def my_task(payload):
    headers = {}
    response = requests.request("POST", "https://test.payu.in/merchant/postservice.php?form=2",headers=headers, data=payload)
    stri = response.content.decode("utf-8")

    #Typecast the string to a dictionary
    dictionary = json.loads(stri)
    print("status>>", dictionary["status"])
    print("msg>>", dictionary["msg"])
    print("Transaction_details>>", dictionary["Transaction_details"])
    print("type>>",type(dictionary["Transaction_details"]))
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db['mycollection1']

# The API quota limit has been reached.
    if dictionary["status"] == 0:
        print("limit reach")
        reschedule_task()
    else:
        collection.insert_many(dictionary["Transaction_details"])
        print("Transaction fetched successfully.")

def reschedule_task(payload):
    my_task.apply_async(args=[payload], countdown=60)


