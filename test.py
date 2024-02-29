from datetime import datetime, timedelta
import urllib  # used for working with URLs and web-related tasks
import json
import logging
from pathlib import Path  # working with file system paths and file operations.
import requests
logging.basicConfig(filename=f"{Path(__name__).resolve().parent}/test.log",
                    level=logging.INFO, format="%(process)d:%(asctime)s:%(levelname)s:%(message)s")

def fetch_dates(start_date, last_date=None):
    dates = {}
    if not last_date:
        last_date = datetime.now()
    start_date = datetime.strptime(start_date, '%d/%m/%Y %H:%M:%S')
    while True:
        end_date = start_date + timedelta(weeks=1)
        dates[start_date.strftime('%d/%m/%Y %H:%M:%S')
              ] = end_date.strftime('%d/%m/%Y %H:%M:%S')
        start_date += timedelta(weeks=1)
        if start_date > last_date:
            break
    return dates

dates = fetch_dates('01/07/2022 00:00:00')
print(len(dates))
for startdate, enddate in dates.items():
    requestparams = {"fromDate": startdate, "toDate": enddate,
                     "pageNumber": 1, "order_Location": 'M01'}
    requestparamstring = json.dumps(requestparams)
    requestparamencode = urllib.parse.quote_plus(requestparamstring)
    payload = "RequestBody=" + requestparamencode + \
        "&ApiOwner=SKCH&ApiKey=77f5c7820bc24e7d8082909b761490339f7ea5208b2946dabb90f3f"
    response = requests.request("POST", "https://skechers.vineretail.com/RestWS/api/eretail/v1/order/orderPull", headers={
        'ApiOwner': 'SKCH',
        'ApiKey': '77f5c7820bc24e7d8082909b761490339f7ea5208b2946dabb90f3f',
        'Content-Type': 'application/x-www-form-urlencoded',
    }, data=payload)
    responsedata = json.loads(response.text.encode('utf8'))
    logging.info(
        f'responsedata : {responsedata} | startdate : {startdate} | enddate : {enddate}')



