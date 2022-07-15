import requests, json, sys, re, os
from datetime import datetime as dt
from dotenv import load_dotenv


path='app/' 
load_dotenv(path+'.env')
IP_nodo = os.getenv('IP_nodo')


"""
 Obtiene el precio actual de Bitcoin en USD de la API de Coindesk y devuelve una cadena con el precio
y la fecha y hora actuales.
Se pueden agregar mas servicios que entreguen un precio como Binance, Bitfinex, Bitstamp, etc.
"""
def precio():
   hoy = dt.strftime(dt.today(), '%d/%b/%Y-%r')
   url = 'http://api.coindesk.com/v1/bpi/currentprice.json'
   r = requests.get(url)
   price  = float(re.sub(',','', r.json()['bpi']['USD']['rate']))
   return '1 Btc vale '+str(round(price,2))+'$ '+hoy+' fuente: Coindesk'
   

"""
   Esta funcion obtiene el último bloque minado. 
   La informacion es tomada de la API que provee RTC BTC explorer, una herramienta 
   que permite visualizar el estado de la red Bitcoin directamente desde el nodo.
   
   Esta se debe configurar para que se pueda acceder a la API de RTC BTC explorer y el procedimiento
   es distinto para cada cliente o aplicación. Para este ejemplo usaremos el API de ejemlo
   - https://github.com/janoside/btc-rpc-explorer     el repositorio de la herramienta.
   - https://bitcoinexplorer.org/api/docs              un demo-live de como corre en cada nodo para test fast.
   En este caso mi nodo umbrel ya esta configurado
   se declara su ip y puerto como variable de entorno
   para seguridad.
   Return: el último bloque en emojis (txt plano estilizado)
"""
def blockclock():
   url = IP_nodo+'/api/blocks/tip/height'
   r = requests.get(url)
   blcl = {'0':'0️⃣','1': '1️⃣', '2':'2️⃣', '3':'3️⃣', '4':'4️⃣', '5':'5️⃣', '6':'6️⃣', '7':'7️⃣', '8':'8️⃣','9':'9️⃣'}
   rspn = ''
   for i in r.text:
      rspn += blcl[i]
   return rspn

# def tx_vol():
#    url = 'http://192.168.1.2:3002/api/tx/volume/24h'
#    r = requests.get(url)
#    return 'Transacciones últimas 24h: '+ str(r.json()['24h'])


def btc_supply():
   url = IP_nodo+'/api/blockchain/coins'
   r = requests.get(url)
   return r.text

def hash_rate():
   url = IP_nodo+'/api/mining/hashrate'
   r = requests.get(url)
   return 'Hashrate: '+str(r.json()['1Day']['val'])+' '+str(r.json()['1Day']['unit'])


def fees():
   '''
   Realiza un calculo de fees in stas/vB para el next block
   '''
   url = IP_nodo+'/api/mempool/fees'
   r = requests.get(url)
   return 'Fee Estimado\nInmediato '+str(r.json()['nextBlock'])+' sats/vB, Una Hora '+str(r.json()['60min'])+' sats/vB'



<<<<<<< HEAD
if __name__=='__main__':
   print(fees())
=======
if __name__=='__main__':   
   print(hash_rate())
>>>>>>> 6ef9ea0 (rpi copy)
