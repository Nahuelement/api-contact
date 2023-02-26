import requests
import time
import datetime

while True:
    req = requests.request('GET', 'https://nahuel-portafolio.herokuapp.com/')
    req1 = requests.request('GET', 'https://job-portal-next.vercel.app/')
    req2 = requests.request('GET', 'https://shop.herokuapp.com/')
    print(req, req1,req2)
    hora_local = datetime.datetime.now()
    print(hora_local.strftime("%H:%M:%S"))
    time.sleep(1200)
