from random import randint 
from telegram import *

updater = Updater(token="505124195:AAGgYoM6EaTH65cSrkUKn4EtWFmpOx-EYeg")
dispatcher = updater.dispatcher

# D4, D6, D8, D10, D12, D20


def rollDice(bot, update):
    diceNumber = int(update.message.text[5:])
    result = randint(1, diceNumber)
    print (result)
    bot.sendMessage(chat_id=update.message.chat_id, text = "You rolled " + str(result))


dispatcher.addTelegramCommandHandler("roll",rollDice)

updater.start_polling()


