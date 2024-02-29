import requests
import time
class RateLimiter:
    def __init__(self, token, requests_per_minute):
        self.token = token
        self.requests_per_minute = requests_per_minute
        self.request_times = []

        # # Make the request with the authentication token
        # headers = {"Authorization": f"token {self.token}"}
        # response = requests.get("https://test.payu.in/merchant/postservice?form=2", headers=headers)
        #
        # # Add the current time to the list of request times
        # self.request_times.append(time.time())
        # return response

# Create a rate limiter with a limit of 5 requests per minute and an authentication token
# limiter = RateLimiter("your_auth_token_here", 10)

# Make 10 requests to the Payumoney API (should be rate-limited for requests 6-10)
# for i in range(10):
#     url = "https://test.payu.in/merchant/postservice?form=2"
#     response = limiter.make_request("https://test.payu.in/merchant/postservice?form=2")
#     if response.status_code == 200:
#         print(f"Request {i+1} succeeded>>  ",{"status":0,"msg":"Requests limit reached"})
#     else:
#         print(f"Request {i+1} failed with status code {response.status_code}")
#
class ApiPulling():
    def __init__(self):
        self.page_number_start = 0

    def GetData(self,page_number_start, page_number, id):
        try:
            total_count = 0
            self.page_number_start = page_number_start
            self.page_number = page_number
            while True:
                # Maximum 10 api could be called in the single task
                if self.page_number - self.page_number_start > 10:
                    Logger('ApiPulling').info(f"page_number Quota Exceeded : page_number => {page_number}")
                    task_id = self.reschedule_task()
                    Logger('ApiPulling').info(f"page_number Quota Exceeded : {self.message} | Task Details : {task_id}")
                    return self.message

                    # make call for the page number
                responsedata = fetchrecords(page_number,id)
                Logger('ApiPulling').info(f"Operation : {self.operation}")
                if responsedata:
                    if responsedata["responseMessage"] == "Success":
                        if bool(responsedata[eRetailStatus.eretail_status[self.operation]]):
                            # check the response data size
                            count = len(responsedata[eRetailStatus.eretail_status[self.operation]])
                            if count > 0: 
                                # make call for the next page
                                data = eRetail.serialize[self.operation].serializedata(responsedata, self.operation)
                                print('data_count :', len(data))
                                Logger('ApiPulling').info(f"data_count : {len(data)}")
                                if data:
                                    try:
                                        addDataQueue(data, copy.deepcopy(self.message))  # * adding data to queue
                                    except Exception as err:
                                        exception_message = str(err)
                                        exception_type, _, exception_traceback = sys.exc_info()
                                        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
                                        Logger('ApiPulling').error(
                                            f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
                                        raise err
                                page_number += 1
                                Logger('ApiPulling').info(f"page_number increment :  {page_number}")
                                self.message['parameter']['page_number'] = page_number
                                total_count = total_count + count
                            else:
                                Logger('ApiPulling').info(f"Breaking loop  {page_number}")
                                break
                        else:
                            Logger('ApiPulling').info(f"Breaking loop, No Data found  {page_number}")
                            break
                    elif responsedata["responseMessage"] == 'No Record Found.':
                        Logger('ApiPulling').info(f"No Records found. Breaking loop  {page_number}")
                        break
                    elif responsedata["responseMessage"] == "Requests limit reached":
                        Logger('ApiPulling').info("Requests limit reached")

                        # Rescheduling the task
                        task_id = self.reschedule_task()

                        Logger('ApiPulling').info(f"Requests limit reached : {self.message} | Task Details : {task_id}")
                        return self.message
                    elif responsedata['responseMessage'] == 'No Records found for matching filters.':
                        Logger('ApiPulling').info(f"No Records found for matching filters. {page_number}")
                        break
                    elif responsedata['responseMessage'] == 'Order Return Not Found':
                        Logger('ApiPulling').info(f"Order Return Not Found. {page_number}")
                        break
                    else:
                        Logger('ApiPulling').info(f"Breaking loop , responseMessage not Success {page_number}")
                        break
                else:
                    Logger('ApiPulling').error(
                        f"Breaking loop , Error while fetching data. Retrying again : {self.message}")
        except Exception as err:
            exception_message = str(err)
            exception_type, _, exception_traceback = sys.exc_info()
            filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
            Logger('ApiPulling').error(
                f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
            raise err

    def reschedule_task(self):
        try:
            return vinreco_works.apply_async(args=[self.message], countdown=600)
        except Exception as err:
            exception_message = str(err)
            exception_type, _, exception_traceback = sys.exc_info()
            filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
            Logger('ApiPulling').error(
                f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
            raise err


# function of fetch records
import requests

def fetchrecords(page_number):
    url = f"https://test.payu.in/merchant/postservice?form=2page_number={page_number}"
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        raise Exception("Error fetching records from API")




