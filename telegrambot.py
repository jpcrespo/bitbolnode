import telebot, json
from telebot import types
import time, os, sys
from dotenv import load_dotenv

load_dotenv('app/.env')

token = os.getenv('token')
master = float(os.getenv('master'))

commands = {'start'  :       'Inicia el bot',
             'help'   :      'Ayuda con el bot'}

knownUsers = []
userStep = {}


menu = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
menu.add('Send IP','OK')

def get_user_step(uid):
       if uid in userStep:      #Busca si existe la llave uid
           return userStep[uid] #y retorna el valor almacenado de ubicacion
       else:
           knownUsers.append(uid)   #En caso de no existir el uid registrado
           userStep[uid] = 0        #se lo almacena y se inicia su ubicacion en cero
           return  userStep[uid]

def listener(messages):
    for m in messages:
        if m.content_type in ["text", "sticker", "pinned_message", "photo", "audio"] :
            with open('/home/umbrel/nodeBot/telegrambot/telegrambot/log_telebot.txt', 'a') as _log:
                _log.write(str(m.chat.id)+'->'+str(m.chat.username)+':'+str(get_user_step(m.chat.id))+'\n')

bot = telebot.TeleBot(token)
#asignamos nuestra funcion listener al bot
bot.set_update_listener(listener)


# START
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid in knownUsers:
        userStep[cid] = 0
        bot.send_message(cid, "Hola 👋👋 "+str(m.chat.username)+" que bueno verte nuevamente.",disable_notification= False)
        time.sleep(0.4)
    else:
        bot.send_message(cid, "Hola 👋👋 "+str(m.chat.username)+', te doy la Bienvenida!',disable_notification= False)
        time.sleep(0.3)
        bot.send_message(cid, "Te voy registrando...",disable_notification= True)
        get_user_step(cid);

    bot.send_message(cid, "Iniciando el bot...",disable_notification= True)
    time.sleep(0.1)
    bot.send_message(cid, "🤖  Listo  ✅... \nPor favor use los botones.",reply_markup=menu,disable_notification= True)

 # AYUDA
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    userStep[cid] = 0
    help_text = "Hola, este bot muestra los datos covid19 en Bolivia\n"
    help_text += "Tambien despliega información de utilidad que se actualiza diariamente.\n"
    help_text += "Comandos disponibles: \n"
    bot.send_message(cid, help_text,reply_markup=menu)
    for key in commands:
        help_textk = "/" + key + ": "
        help_textk += commands[key] + "\n"
        bot.send_message(cid, help_textk,reply_markup=menu)

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 0)
def main_menu(m):
    cid = m.chat.id
    text = m.text
    if text == "Send IP":
        if cid == master:
            os.popen('ifconfig > ip.txt')
            time.sleep(2)
            with open('ip.txt','rb') as ips:
                bot.send_document(master,ips,reply_markup=menu)
            time.sleep(2)
            os.remove('ip.txt')
            userStep[cid] = 0
        else:
            bot.send_message(cid,'Solo yo puedo Rox. Solo yo',reply_markup=menu)

    elif text == "OK":  # CAMARA
        with open('/home/umbrel/nodeBot/telegrambot/telegrambot/btc.txt') as ips:
            bot.send_document(cid,ips, reply_markup=menu)
            userStep[cid] = 0



# MENU PRINCIPAL


def main_loop():
    print('Corriendo...')
    bot.polling(True)


if __name__ == '__main__':
        try:
                main_loop()
        except KeyboardInterrupt:
                print('\nExiting by user request.\n')
