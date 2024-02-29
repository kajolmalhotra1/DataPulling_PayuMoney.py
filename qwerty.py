import requests

url = "https://test.payu.in/merchant/postservice.php?form=2"

payload = {'key': 'JPM7Fg',
'command': 'get_transaction_details',
'var1': '2020-10-20',
'var2': '2020-10-27',
'hash': '0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
