#!/usr/bin/python

import time, datetime
import telepot
from telepot.loop import MessageLoop
from apscheduler.schedulers.background import BackgroundScheduler
import os, sys
import argparse
import logging
import requests


def parse_args():
    parser = argparse.ArgumentParser(description='PythonBot for morning info ')
    #parser.add_argument('--nrfiles', type=int, default=1)
    return parser.parse_args()



def quote():
    url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
    response = requests.get(url)
    data = response.json()
    return data['thought']["quote"]

def joke():
    url = "https://geek-jokes.sameerkumar.website/api"
    response = requests.get(url)
    return response.content


def sendSimpleText(chat_id):
    telegram_bot.sendMessage(chat_id,str('faez'))




def action(msg):
    chat_id = msg['chat']['id']
    command  = msg['text']

    now = datetime.datetime.today()

    print "Received: %s " %command

    if command == '/hi':
        telegram_bot.sendMessage(chat_id, str("Hi there! I'm your morning assistant"))
    elif command == '/help':
        help_message = "Help message for the weather bot. \n /hi \n /help \n /date \n /today \n /weather \n /quote \n "
        telegram_bot.sendMessage(chat_id, help_message)
    elif command == '/date':
        telegram_bot.sendMessage(chat_id, str(now.strftime("%d/%m/%Y")))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.strftime("%H:%M:%S")))
    elif command == '/today':
        telegram_bot.sendMessage(chat_id, str(now.strftime("%d/%m/%Y -- %H:%M:%S")))
    elif command == '/weather':
        telegram_bot.sendPhoto(chat_id, photo = "http://www.yr.no/place/Switzerland/Gen%C3%A8ve/Geneva~6458783/meteogram.png")
    elif command == '/quote':
        telegram_bot.sendMessage(chat_id, str(quote()))
    elif command == '/joke':
        telegram_bot.sendMessage(chat_id, joke())



def main():
    args=parse_args()

    print(telegram_bot.getMe())
    MessageLoop(telegram_bot, action).run_as_thread()

    print "Up and Running"

    while 1:
        time.sleep(10)



if __name__ == "__main__":
    telegram_bot = telepot.Bot('TELEGRAM_BOT_TOKEN')
    main()
