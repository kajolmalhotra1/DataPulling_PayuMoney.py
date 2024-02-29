import os

#  To define a consistent set of error codes that can be used throughout an application or system.

class ErrorCodes:
    Unset = 100  # error code has not been set. the required parameter is missing or invalid
    DatabaseError = 101  # error has been occurred while interacting with a database.
    WrongCredentials = 102  # username and password are invalid
    InternalError = 103  # unexpected error occurred within the API system
    EmptyCred = 104  # indicate that the credentials required for authentication with the API have not provided
    Blocked = 105  # user or client making the request has been blocked from accessing the API
    CookieExpired = 106  # cookie used for authentication or session management has been expired
    ParamErr = 107  # error in the parameters provided with the API request
    LoginSuccessful = 108  # indicate that a user has successfully authenticated and logged in to the API
    EmptyResponse = 109  # indicate that an API request was successful,but no data was returned in the response
    NoEntriesToProcess = 110  # indicate that an API request was successful,but there are no entries left to process
    EntriesFound = 111  # indicate that an API request was successful, and one or more entries were found
    Successful = 200  # indicate that an API request was successful and the operation was completed as expected.
    NotFound = 404  # indicate that the resource or endpoint requested by the API client was not found.
    InvalidCredentials = 112  # indicate that the authentication credentials supplied by the API client were invalid
    ApiHitQuotaExceeded = 113  # indicate that the API client has exceeded rate limit for no of requests within time period.

    # code sets up the connection to the mongodb Database
    # checks for the value of the environment variable 'STAGE' using the os.getenv method and prints it
    print(os.getenv('STAGE'))

    # 'STAGE' is 'dev', the code sets environment variables related to database connections.
    # if os.getenv('STAGE') == 'dev': #method in Python returns the value of the environment variable key if it exists otherwise returns the default value.
    os.environ[
        "PUSH_DATA_URL"] = "mongodb://localhost:27017/Vinstore?authSource=admin"  # authentication source for the database,which is admin
    os.environ["PUSH_DATA_DB"] = "vinstore_local"  # pushing data
    os.environ[
        "FETCH_DATA_URL"] = "mongodb://localhost:27017/Vinstore?authSource=admin"  # environment variables point to the same database
    os.environ["FETCH_DATA_DB"] = "vinstore_local"  # fetching data


# stores the MongoDB database URLs for pushing and fetching data. The URLs are stored as class attributes push_data_url and fetch_data_url
class DBURL:
    push_data_url = os.getenv('PUSH_DATA_URL')
    fetch_data_url = os.getenv('FETCH_DATA_URL')

# Define a Python class DB with two class attributes fetch_data_db and push_data_db
class DB:
    fetch_data_db = os.getenv('FETCH_DATA_DB')
    push_data_db = os.getenv('PUSH_DATA_DB')

# PullType variable is used to specify what type of data to pull from a data source or API
PullType = ["ORDERS"]

# The key is "ORDERS" and the value is "eretailOrders"
# when data is pulled for the "ORDERS" pull type, it will be stored in the "eretailOrders" collection in the MongoDB database.
CollNames = {
    "ORDERS":"eretailOrders"
        }


