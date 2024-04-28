import requests

url = 'http://localhost:8899'

headers = {
    # "X-API-KEY": 'aa-aa-00-aa',
    "Content-Type": "application/json"
    }

json_data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTransaction",
    "params": [
        "2ch8VvmLsFioFm8dfnokH6xqUZ6xw3Lv1xZx6s8ptZB58BQPfUQ1oaCHfYakVMjHFaa1pdk5g8n4XSqo1ypj9CQ7",
        {
            "maxSupportedTransactionVersion": 0
        }
    ]
}

response = requests.request(
    method='post',
    url=url,
    headers=headers,
    json=json_data
)

print(response.text)

with open('j.json', 'w') as file:
    import json
    json.dump(response.json(), file, indent=4)