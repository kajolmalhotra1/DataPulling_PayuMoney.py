from mongodb_vinreco.mongodbops import *
from logs import Logger
from Global import CollNames
from datetime import date, datetime
from Global import DBURL, DB

# The 'addDataQueue' function appears to be a custom function that takes in two arguments: data and message.
def addDataQueue(data, message):
    try:   
        message.update(message['parameter'])
        message.update({'endt': str(date.today()), 'endttm': datetime.now()})
        operation = message['operation']
        [message.pop(key) for key in ['operation', 'apikey', 'apiowner', 'parameter']]
        extended_data = list(map(lambda x: {**message, **x}, data)) # function created a new list called 'extended_data' which contains the 'message dictionary' merged with each dictonary in 'data' list.
        data_push(CollNames[operation], extended_data)
        Logger('addDataQueue').info(f'Message : {message} | operation : {operation}')
    except Exception as e:
        exception_message = str(e)
        exception_type, _, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logger('addDataQueue').error(
            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        raise e

# 'data_push' function is used to push data into mongodb database
def data_push(coll, data): # which represents the name of collection to insert the data.
    """                    # which is the list of dictionaries containing the data to be inserted.
    Push data to the DB
    """
    try:
        client = MongoDBConnector(DBURL.push_data_url, DB.push_data_db) # a MongoDBConnector object is created with the URL and database name as arguments
        client.make_connection_url() # method is then called on the 'client' object to establish a connection to the database.
        client.insert_many(coll, data) # method is called on the client object to insert the data into the specified collection.
    except Exception as e:
        exception_message = str(e)
        exception_type, _, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        Logger('data_push').error(
        f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")





