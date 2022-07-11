'''
Este script recopila a los últimos 5 seguidores, descarga sus fotos de perfil, crea un banner
personalizado lo sube y actualiza el nombre de usuario al último bloque verificado por el nodo.
'''
from twlogin import login
from PIL import Image, ImageDraw, ImageFont
import os, requests


def 5last(target='boliviabitcoin'):
   api = login()
   user = api.get_user(screen_name=target)
   for follower in user.followers()[:5]:
      target  = follower._json['profile_image_url']
      #commando = 'wget -O '+'/home/ghost/Desktop/proyectos/twitter/twbot/banner/banner/'+follower._json['screen_name'][:]+'.jpg'+' '+target
   # os.system(commando);
   banner()

def banner():
   #creamos la imagen

   #banner de twitter sugiere estas medidas
   WIDTH = 1500
   HEIGHT = 500
   SIZE = (WIDTH, HEIGHT)
   fondo = (5,5,5)
   image = Image.new('RGB', SIZE, fondo)

   wpp  = Image.open('wpp.png')
   pos = (650,170)
   image.paste(wpp, pos)

   # Para el texto:

   #TITULO
   text_color = (250,250,250)
   TEXT_FONT_TYPE = ('MonoLisaSimpson-Regular.ttf')
   TEXT_SIZE = 55
   TEXT_PADDING_HOR = 550
   TEXT_PADDING_VERT = 50
   IMG_TEXT = 'WELCOME!'
   draw = ImageDraw.Draw(image)
   font = ImageFont.truetype(TEXT_FONT_TYPE, TEXT_SIZE)
   offset_text = (TEXT_PADDING_HOR, TEXT_PADDING_VERT)
   draw.text(offset_text, IMG_TEXT, text_color, font=font)

   #hora de Bitcoin
   url = 'https://blockchain.info/latestblock'
   r = requests.get(url)
   blockclock = r.json()['height']
   TEXT_SIZE = 30
   TEXT_PADDING_HOR = 45
   TEXT_PADDING_VERT = 130
   IMG_TEXT = 'A special greeting\n\nfor my last 5 followers:\n'

   draw = ImageDraw.Draw(image)
   font = ImageFont.truetype(TEXT_FONT_TYPE, TEXT_SIZE)
   offset_text = (TEXT_PADDING_HOR, TEXT_PADDING_VERT)
   draw.text(offset_text, IMG_TEXT, text_color, font=font)

