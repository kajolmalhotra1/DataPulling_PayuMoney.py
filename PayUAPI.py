from API.PayUMoney_class import PayUAPI
# PayUAPI instance is initialized with the API key and API secret
api = PayUAPI(api_key="my_api_key", api_secret="my_api_secret")

try:
    # make_request method is used to send a GET request to the /api/orders endpoint
    response = api.make_request(method="GET", endpoint="/api/orders")
    print(response) # print the JSON response returned by the make request method
except Exception as e:
    print(f"Error: {e}")





