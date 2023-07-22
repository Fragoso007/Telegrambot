
import telebot 
KEY_API = '6687550589:AAFadHZIWqtiFp9ta8a0vOlSs9JoSObSuaQ'

bot = telebot.TeleBot(KEY_API)


@bot.message_handler(commands=['Iphone_12_Pro_Max'])
def Iphone_12_Pro_Max(messag):
    bot.send_message(messag.chat.id, 'This is an excellent option')

@bot.message_handler(commands=['Iphone_13_Pro_Max'])
def Iphone_13_Pro_Max(messag):
    bot.send_message(messag.chat.id, 'How wonderful, this is one of the best sellers')

@bot.message_handler(commands=['Iphone_14_Pro_Max'])
def IIphone_14_Pro_Max(messag):
    bot.send_message(messag.chat.id, 'Very good, this is the latest model available')

@bot.message_handler(commands=['option1'])
def option1(messag):
    text ='''
    What do you want? (choose an option)
    /Iphone_12_Pro_Max
    /Iphone_13_Pro_Max
    /Iphone_14_Pro_Max '''
    bot.send_message(messag.chat.id, text)

@bot.message_handler(commands=['option2'])
def option2(messag):
    bot.send_message(messag.chat.id, 'To complain about an order, send e email to antoniofragoso583@gmail.com')


@bot.message_handler(commands=['option3'])
def option3(messag):
    bot.send_message(messag.chat.id, 'Thanks, Fragoso said Hi to you too')


def verif(messag):
    return True

@bot.message_handler(func=verif)
def answer(messag):
    text = '''
    Choose an option to continue (click on the item):
    /option1 make a request
    /option2 complain about an order
    /option3 send a hug to Fragoso
    Answering anything else will not work, choose one of the options'''
    bot.reply_to(messag, text)

bot.polling()
