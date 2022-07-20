
import requests, json, os, re 
import numpy as np
from dotenv import load_dotenv
from datetime import datetime as dt
from twlogin import login

#path='/home/ghost/Desktop/proyectos/'
load_dotenv('.env')
IP_nodo = os.getenv('IP_nodo')

hoy = dt.strftime(dt.today(), '%d/%b/%Y')

#una idea es crear un archivo npy con un array
#de estados actualizados a diario para elegir algunos tuits
#con más seguimiento e información.

#El archivo estados.npy se creo con un array de un solo elemento:
#el ultimo precio diario registrado 

price = np.load('estados.npy',allow_pickle='TRUE').tolist()



message = f'''Los datos #Bitcoin de hoy 📅 {hoy}:\n''' 

url = 'http://api.coindesk.com/v1/bpi/currentprice.json'
r = requests.get(url)
aux = float(re.sub(',','', r.json()['bpi']['USD']['rate']))



if aux > price:
  message += '\n➯ Precio: 📈 1 ₿tc = '+str(round(aux,2))+' USD'
else:
  message += '\n➯ Precio: 📉 1 ₿tc = '+str(round(aux,2))+' USD'

np.save('estados.npy',aux)


url = IP_nodo+'/api/blockchain/coins'
r = requests.get(url)
a = float(r.text)
b = round(100*a/21_000_000,5)

message += '\n➯ ₿tc emitido: '+str(round(a,3))+' ('+str(b)+'%)'


url = 'https://bitcoinexplorer.org/api/tx/volume/24h'
r = requests.get(url)
aux = r.json()['24h']

message += '\n➯ Tx últimas 24h: '+str(aux)



halving_in = 630000
halving_out = 840000
url = IP_nodo+'/api/blocks/tip/height'
r = requests.get(url)
c = int(r.text) - halving_in
d = halving_out - halving_in
halv = round(10*c/d)
progress = ''
for a in range(0,10):
   if a<halv:
      progress += '▒'
   else: 
      progress += '▩'
progress += ' '

message += '\n➯ Halving en proceso: ' +progress+str(round(100*c/d,2))+'% (~4/abril/24)'
message += '\n\n                 𝕀 ℕ   ℂ 𝕆 𝔻 𝔼   𝕎 𝔼   𝕋 ℝ 𝕌 𝕊 𝕋'


api = login()


api.update_status(status=message)

print(message)