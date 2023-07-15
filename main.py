import requests
import time

def send_request():
    # Send your HTTP request here
    response = requests.get("https://mt4tradingbot-ojwc.onrender.com/")
    print(response.text)

while True:
    send_request()
    time.sleep(20)
