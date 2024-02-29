from pulling_tasks import vinreco_works
from Global import DBURL, DB,CollNames
from datetime import datetime, timedelta,date
# from logs import Logger
from celery import Celery

app = Celery('Test app', broker='redis://localhost:6379/0')

def fetch_dates(start_date, last_date=None):
    dates = {}
    if not last_date:
        last_date = datetime.now()
    else:
        last_date = datetime.strptime(last_date, '%d/%m/%Y %H:%M:%S')
    start_date = datetime.strptime(start_date, '%d/%m/%Y %H:%M:%S')
    while True:
        end_date = start_date + timedelta(weeks=1)
        dates[start_date.strftime('%d/%m/%Y %H:%M:%S')] = end_date.strftime('%d/%m/%Y %H:%M:%S')
        start_date += timedelta(weeks=1)
        if start_date > last_date:
            break
    return dates

class eRetailOrders:

 def __init__(self, api_subdomain, api_owner, api_key):
        self.api_subdomain= api_subdomain
        self.api_owner= api_owner
        self.api_key=api_key
        self.channel_id='CHANNEL_ID'
        self.client_id='CLIENT_ID'

def main(self):
           dates = fetch_dates('01/01/2020 00:00:00')
           print('Total Length of dates :', len(dates))
           for start_date, end_date in dates.items():
               message = {
                   "source": 'VinStore',
                   "client_id": self.client_id,
                   "messageid": 'uuid',
                   "account_id": self.account_id,
                   "Report": 'ORDERS',
                   "Call for": 'Data Pulling',
                   "api_key": self.api_key,
                   "api_owner": self.api_owner,
                   "api_subdomain": self.api_subdomain,
                   "parameter": {
                       "from_date": start_date,
                       "to_date": end_date,
                       "Orders": [],
                       "page_number": 1
                   }
               }

PullType= ["ORDERS"]

# current module has been executed for the main program
if __name__ == "__main__":
    API_KEY = '77f5c7820bc24e7d8082909b761490339f7ea5208b2946dabb90f3f'
    API_OWNER = 'SKCH'
    API_SUBDOMAIN = 'skechers'
    CLIENT_ID = 1
    ACCOUNT_ID = 1


# #entrypoint
# task_id = vinreco_works.delay(message)
# Logger("eRetailOrders").info(f"Message : {message} | Task Details : {task_id}")
# exit(0)


# @app.task
# def vinreco_works(message):
#    task_id = vinreco_works.delay(message)
# pass

task_id = vinreco_works.delay(message)
print("==>> task_id: ", task_id)






