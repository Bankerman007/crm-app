import requests

class Api_Call:

    def rates(self):
        response = requests.get('http://fast-api-rates.justdev.us/rates/1')
        json_convert= response.json()
        json_data= json_convert['rate']
        rate = json_data['rate']

        return rate

    def prime_rate(self):
        response = requests.get('http://fast-api-rates.justdev.us/rates/2')
        json_convert= response.json()
        json_data= json_convert['rate']
        prime = json_data['rate']
        
        return prime     

    def dow(self):
        response = requests.get('http://fast-api-rates.justdev.us/rates/4')
        json_convert= response.json()
        json_data= json_convert['rate']
        dow_price = json_data['rate']
            
        return dow_price

    def dow_price_change(self):
        response = requests.get('http://fast-api-rates.justdev.us/rates/3')
        json_convert= response.json()
        json_data= json_convert['rate']
        dow_price_diff = json_data['rate']
        
        return dow_price_diff