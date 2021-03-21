# instalamos la libreria del bot para telegram
# pip install pyTelegramBotAPI
# importamos la libreria del Bot de telegram
import telebot
# instalamos la libreria de Flask
# pip install Flask
# importamos Flask para montar el servidor en el que ira el bot
from flask import Flask
# para correr el servidor necesitamos agregar la aplicacion en las variables de entorno de FLASK_APP
# $env:FLASK_APP = "Documento"

app = Flask(__name__)
# Accedemos al Bot por medio de nuestro token
bot = telebot.TeleBot('')
# Esta es una prueba de como el bot le daria la bienvenida a una persona a la conversacion
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
# Para crear encuestas lo que hare sera meter toda la informacion en un archivo que python creara o buscara
# este archivo almacenara todas las encuestas en un json 
@bot.message_handler(commands=['crear'])
# funcion dentro del handler que reacciona a mensajes enviados hacia el bot
def crear_Encuesta(message):
    # esta clase nos permite declarar que usaremos un teclado especial para que el usuario pueda responder de forma sencilla la pregunta
    teclado = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # aqui agregamos a la clase en un arreglo las posibles respuestas del usuario
    # en este caso usamos / para que al responder el usuario un comando mas salte a su respuesta
    teclado.add('/si', '/no')
    # El mensaje es enviado con la funcion reply_to que usar de destino el mismo mensaje al que esta reaccionando y envia el teclado que preparamos para responde
    bot.reply_to(message, 'Eres major de Edad?', reply_markup=teclado)

# handler que esta esperando el mensaje de la respuesta 
@bot.message_handler(commands=['si', 'no'])
def pregunta_Principal(message):
    # usamos un try..catch para gestionar los errores que se generen en el api mientras se procesa la informacion
    try:
        # procesamos el mensaje para saber que responder al mensaje de respuesta 
        if str(message.text) == '/si':
            response = 'Si eres mayor de edad'
            bot.reply_to(message, response)
        else:
            response = 'No eres mayor de edad'
            bot.reply_to(message, response)    
    # esta es la funcion que nos permite saber si ha habido algun error dentro del try y asi poder responder algo al usuario 
    except:
        bot.reply_to(message, 'algo salio mal, espera')

# la funcion polling no es mas que el inicio de bot, sin esto el bot no funcionaria 
bot.polling()

# declaracion de rutas para el api de FLASK
@app.route('/')
def hello_world():
    # respuesta de la ruta '/'
    return 'This is a Bot API'
