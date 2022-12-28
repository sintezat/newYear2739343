import telebot
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
from os import path, system


if __name__ == '__main__':
    if not path.isfile('data'):
        f = open('data', 'w')
        f.close()

    dayEndsWith = {'й': [8,7,6,5,0]}
    hourEndsWith = {'а': [2,3,4,22,23]}
    minsecEndsWith = {'а': [1,21,31,41,51],
                      'ы': [2,3,4,22,23,24,32,33,34,42,43,44,52,53,54]}
    bot = telebot.TeleBot('5844491437:AAHp0Ycgb8VuAHY-9WpG_r-u7RTzdGogFuw')


@bot.message_handler(commands=['start'])
def start(message):
    chatIdSaver(str(message.chat.id))
    bot.send_message(message.chat.id, getTimeDelta())


def chatIdSaver(chatid):
    t = open('data', 'r').read()
    with open('data', 'a') as f:
        if chatid not in t:
            f.write(chatid + '\n')


def sendGreeting():
    with open('data', 'r') as f:
        for x in f.readlines():
            bot.send_message(int(x), 'С НГ!!!!!!!!!!!!!!!!!!!!!!!111')


def getTimeDelta():
    delta = datetime(2023, 1, 1, 0, 0, 1) - datetime.now()
    hms = [int(x) for x in str(delta).split(', ')[1].split('.')[0].split(':')]

    if delta.days in dayEndsWith['й']: days = 'дней'
    elif delta.days == 1: days = 'день'
    else: days = 'дня'

    if hms[0] in hourEndsWith['а']: hours = 'часа'
    elif hms[0] in (1, 21): hours = 'час'
    else: hours = 'часов'
    
    if hms[1] in minsecEndsWith['а']: minutes = 'минута'
    elif hms[1] in minsecEndsWith['ы']: minutes = 'минуты'
    else: minutes = 'минут'
    
    if hms[2] in minsecEndsWith['а']: seconds = 'сукунда'
    elif hms[2] in minsecEndsWith['ы']: seconds = 'секунды'
    else: seconds = 'секунд'

    return f'До Нового года {delta.days} {days} {hms[0]} {hours} {hms[1]} {minutes} {hms[2]} {seconds}'


def main():
    bot.polling(none_stop=True, interval=0)
    return


def timer():
    sleep(5)
    while True:
        if datetime(2023, 1, 1, 0, 0, 1) - datetime.now() <= timedelta(seconds=5):
            sendGreeting()
            system('pkill python')
        sleep(1)


thread1 = Thread(target=timer).start()
thread2 = Thread(target=main).start()
