#!/usr/bin/python3
# coding: utf-8
# Developed by Tiago Neves
# Github: https://github.com/TiagoANeves
# Version: 1.0
# All rights reserved

#Import necessary modules
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
import subprocess
import os

# Get your UserName 
def whoami(bot, update): 
    nome = update.message.chat.username
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=nome)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

# Just an example to parse another URL and send the content.
def dog(bot, update):
    chat_id = update.message.chat_id
    if update.message.chat.username == validuser:    
        url = get_image_url()
        bot.send_message(chat_id=chat_id, text="Segue a foto do catioro!")
        bot.send_photo(chat_id=chat_id, photo=url)
    else:
        bot.send_message(chat_id=chat_id, text="Usuário não permitido!")

# Runs any command on linux, Be careful
def opencmd(bot, update):
    if update.message.chat.username == validuser:
        saida = subprocess.getoutput(update.message.text.lower())
        bot.send_message(chat_id=update.message.chat_id, text=saida)

# Runs any command on linux. Be careful
def cmd(bot, update, args):
    chat_id = update.message.chat_id
    if update.message.chat.username == validuser:
       cmd_exec = ' '.join(args).lower()
       saida = subprocess.getoutput(cmd_exec)
       bot.send_message(chat_id=update.message.chat_id, text=saida)

# Check Disk, Memory and CPU Load
def check(bot, update, args):
    chat_id = update.message.chat_id
    if update.message.chat.username == validuser:
        cmd_exec = ' '.join(args).lower()
        if cmd_exec == 'disk':
            saida = subprocess.getoutput('df -h')
            bot.send_message(chat_id=update.message.chat_id, text=saida)
        elif cmd_exec == 'memory':
            saida = subprocess.getoutput('free -m')
            bot.send_message(chat_id=update.message.chat_id, text=saida)
        elif cmd_exec == 'cpu':
            saida = subprocess.getoutput('uptime')
            bot.send_message(chat_id=update.message.chat_id, text=saida)

# Send the available commands.
def helpme(bot, update):
    chat_id = update.message.chat_id
    if update.message.chat.username == validuser:
        bot.send_message(chat_id=update.message.chat_id, text="Comandos Configuados: \
										\n/help \
										\n/dog \
										\n/cmd <comando> Só use se souber o que está fazendo! \
										\n/check (disk, memory, cpu)")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comandos Configuados: \n/help\n/dog")

# Main - Define the Handler.
def main():
    global validuser 
    # Valid user to run commands.
    validuser = '<USER>'
    # Bot token
    updater = Updater('<BotToken>')
    dp = updater.dispatcher
    # Command Handler
    dp.add_handler(CommandHandler('dog', dog))
    dp.add_handler(CommandHandler('whoami', whoami))
    dp.add_handler(CommandHandler('help', helpme))
    dp.add_handler(CommandHandler('start', helpme))
    dp.add_handler(CommandHandler('cmd', cmd, pass_args=True))
    dp.add_handler(CommandHandler('check', check, pass_args=True))
    # Message Handle, you can run any commands on linux machine. Be careful
    dp.add_handler(MessageHandler(Filters.text, opencmd))
    updater.start_polling()
    updater.idle()

# Main
if __name__ == '__main__':
    main()
