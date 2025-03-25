import os

class Config:
    SECRET_KEY = os.urandom(24)  
    API_KEY = ''  
    BASE_URL = 'https://api.coingecko.com/api/v3'  
