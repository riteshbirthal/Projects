import requests

def light_on():
  requests.get('http://172.24.192.5/on2')
  # requests.get('http://172.24.192.5/on2')
    
def devil_on():
  requests.get('http://172.24.192.5/on1')
  # requests.get('http://172.24.192.5/on1')
    
def lights_off():
  requests.get('http://172.24.192.5/offall')
  # requests.get('http://172.24.192.5/offall')
  #urllib3.PoolManager().request('GET', "http://172.24.192.5/offall")
