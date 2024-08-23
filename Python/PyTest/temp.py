import requests

def func():
    return "hello world"

class CustomError(Exception):
    status_code = 412
    message = "Custom Error"


def my_function(data):
    if not data:
        raise CustomError(1001)
    
    response = requests.post("https://www.google.com/", json=data)
    return response.json()