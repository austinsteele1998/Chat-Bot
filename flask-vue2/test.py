

# In this file,

# 1) Figure out how to put flask app up that just return the string that was
# passed in

# 2) Use the request package make api call to get respoonse

import requests
import json

url = 'http://localhost:5000/dummy_chat'
m_str = {'message': "Hello Json"}



# A function that sends a request to the flask chat endpoint and prints out the response

def query_flask(m):
    m_str2 = {'message':m}
    t=requests.post(url, json=m_str2).json()
    print(t['message'])
    return t['message']


str="hello Time 1234"
t2=query_flask(str)


