import requests

def rates():
    response = requests.get('http://fast-api-rates.justdev.us/rates/1')
    json_convert= response.json()
    json_data= json_convert['rate']
    rate = json_data['rate']

    return rate

rates()

def prime_rate():
    response = requests.get('http://fast-api-rates.justdev.us/rates/2')
    json_convert= response.json()
    json_data= json_convert['rate']
    prime = json_data['rate']
    
    return prime 

prime_rate()  

def dow():
    response = requests.get('http://fast-api-rates.justdev.us/rates/4')
    json_convert= response.json()
    json_data= json_convert['rate']
    dow_price = json_data['rate']
        
    return dow_price

dow()

def dow_price_change():
    response = requests.get('http://fast-api-rates.justdev.us/rates/3')
    json_convert= response.json()
    json_data= json_convert['rate']
    dow_price_diff = json_data['rate']
    print(dow_price_diff)

    return dow_price_diff

dow_price_change()
