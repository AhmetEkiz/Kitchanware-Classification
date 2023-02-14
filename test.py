import requests

# local url
# url = "http://localhost:8080/2015-03-31/functions/function/invocations"

# AWS API Gateway for Kitchenware Classification
url = "{your API URL}"

data = {'url' : 'https://images.unsplash.com/photo-1542838309-fbfad201ce6d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjh8fGZvcmt8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60'}

result = requests.post(url, json=data).json()
print(result)