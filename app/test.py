''' 
Este Script recopila los 3200 tuits mas recientes de un target y genera:
1. user_info.txt file - Toda la información disponible de contacto
2. user_historial.csv file - Un csv con los tuits: fecha y texto.
'''

from dotenv import load_dotenv
import os, tweepy, csv, pytz
from datetime import datetime

load_dotenv('.env')

API_KEY = os.getenv('API_Key')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

print('Iniciamos autentificación con Twitter API')
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Autentificación... sesión iniciada  ok!")
except:
    print("No se logra iniciar sesión, ERROR!")
   

description = 'test 1'
#api.update_profile(description=description)
api.update_status(description)
