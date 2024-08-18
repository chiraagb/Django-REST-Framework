import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"


# get_response = requests.get(endpoint, json={"query": "Hello world"})  # HTTP Request
get_response = requests.get(endpoint, data={"query": "Hello world"})  # HTTP Requests

print(get_response.text)  # print raw text response : it is a json

"""
TODO: 
    1HTTP Request -> Returns HTML, CSS, JS
    2.REST API HTTP Request -> Returns JSON
    3.JSON -> JavaScript Object Notation ~ Python Dictionary
"""

print(get_response.json())  # print json response : it is a dictionary
print(get_response.status_code)  # print status code


# TODO: What you send is what you receive
