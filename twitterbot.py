# Este script ejecuta un bot de twitter con la capacidad de 
# estar escuchando menciones de otros usuarios de twitter.
# Dependiendo del comando puede entregar respuestas

from time import sleep
from app.twlogin import login
from app.tools import blockclock, precio , btc_supply, hash_rate, fees
import numpy as np
import sys, os


def execute(order):
   txt = order._json['full_text'].lower()
   txt_split= txt.split(" ")    #cambia este valor segun el nombre @user
   for word in txt_split:
      if word in ['blockclock','btcclock','btc_clock','clock','tic']:
         api.update_status(status='@'+order._json['user']['screen_name']+' '+blockclock(),in_reply_to_status_id=order._json['id_str'],auto_populate_reply_metadata=True)
         return order._json['id_str']
      elif word in ['btc_supply','supply','emitido','btc_emitido','btc_emision','emision','emision_btc']:
         api.update_status(status='@'+order._json['user']['screen_name']+' '+btc_supply(),in_reply_to_status_id=order._json['id_str'],auto_populate_reply_metadata=True)
         return order._json['id_str']
      elif word in ['hash_rate','hash-rate']:
         api.update_status(status='@'+order._json['user']['screen_name']+' '+hash_rate(),in_reply_to_status_id=order._json['id_str'],auto_populate_reply_metadata=True)
         return order._json['id_str']
      elif word == 'fees':
         api.update_status(status='@'+order._json['user']['screen_name']+' '+fees(),in_reply_to_status_id=order._json['id_str'],auto_populate_reply_metadata=True)
         return order._json['id_str']
      elif word in ['precio','btc_price','bitcoin_precio']:
         api.update_status(status='@'+order._json['user']['screen_name']+' '+precio(),in_reply_to_status_id=order._json['id_str'],auto_populate_reply_metadata=True)
         return order._json['id_str']
         #retorna el id donde responde, o False en caso de que no haya un comando.
   return False




# A diferencia de otros métodos, este obtiene las ultimas 20 menciones
# incluidos rt sin Cursor. Se puede modificar la recuperación de 20 dependiento de 
# la fecha de inicio y fin de la búsqueda. 

# Para controlar un flujo y evitar responder menciones repetidas, usamos un archivo
# externo para almacenar el id de las menciones anteriores. Por facilidad en recuperar
# y escribir un log usamos numpy y .npy 

def first_up(path=''):
   #la primera vez que se ejecuta el bot, verifica si existe un log.
   #En caso de que no, realiza el analisis:
   ids = [] #en esta variable guardamos id de respuestas para el log
   #recopila las últimas 20 menciones
   historial = api.mentions_timeline(tweet_mode='extended')
   #verifica que historial no sea una lista vacia
   if len(historial) == 0:
      #en caso de que sí, crea el log vacío.
      np.save(path+'respuestas.npy', ids)
   else:
      #en caso de que hayan meciones 
      for order in historial[::-1]:
         aux = execute(order)
         if not aux:
            pass
         else: 
            ids.append(aux)
   #finalmente guardamos el log 
      np.save(path+'respuestas.npy', ids)





def main(p1=''):
#verificamos si existe un log
   if not os.path.exists(p1+'respuestas.npy'):
      # primer analisis si es que no
      first_up(path=p1) 
   else:
      # resp cuando ya existe puede ser estar vacio eventualmente
      # para nuevas menciones solo se necesita rescatar
      # el valor mas reciente de la lista y solo procesará
      # nuevas menciones. 
      resp = np.load(p1+'respuestas.npy',allow_pickle='TRUE').tolist()
      if not resp: #podria pasar que resp sea una lista vacia
         #en este caso llamamos a la api igual que en first_up
         historial = api.mentions_timeline(tweet_mode='extended')
         if len(historial)==0:  #si no hay nada, no pasa nada
            pass
         else:
            for order in historial[::-1]:
               aux = execute(order)
               if aux:
                  resp.append(aux)
               else:
                  pass
      else: 
         #recuperamos la ultima mención del log para iniciar desde ese id para adelante
         #puede darse el caso de que las menciones sean >20 por lo que se deja al bot en bucle
         #para q vaya procesando por bloques de 20.
         historial = api.mentions_timeline(tweet_mode='extended',since_id=resp[-1])
         for order in historial[::-1]:
            resp.append(execute(order))   
      np.save(p1+'respuestas.npy', resp)



if __name__ == "__main__":
   #para automatizar un proceso este método es sugerido en python:
   #llamar a una función main() con excepciones para volver a ejecutar el programa.
   p_env='/home/ghost/Desktop/proyectos/'
   api = login(path=p_env)
   while True:
      try:
         main(p1='/home/ghost/Desktop/proyectos/bots/bitbolnode/app/')
      except KeyboardInterrupt:
         print('Exiting by user request.\n')
         sys.exit(0)
      finally:
         sleep(240)
