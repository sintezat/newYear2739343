# -*- coding: utf-8 -*-
XXX = 0

import telebot
from datetime import *
import time
import pytz

def taimer():
    tz = pytz.timezone('Europe/Moscow')
    a = str(datetime.now(tz)).split()[0].split('-') + str(datetime.now(tz)).split()[1].split(':')
    a.pop(-1)
    a[-1] = a[-1][:2]
    for i in range(len(a)):
        a[i] =int(a[i])

    s = a[-1] + a[-2]*60 + a[-3]*3600 + a[-4]*3600*24
    if 0 < s < 100:
        print('с НГ')  #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        XXX = 1
    s = 2678400 - s
    d = s//(3600*24)
    ch = (s - d*(3600*24))//3600
    mi = (s % 3600)//60
    sek = s%60

    q = [8,7,6,5,0]
    qq = [3,4,2]
    if d == 1:
        d1 = 'день'
    elif d in q:
        d1 = 'дней'
    elif d in qq:
        d1 = 'дня'
    else:
        d1 = 'дня'

    q = [2,3,4,22,23]
    qq = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    if ch == 1 or ch == 21:
        ch1 = 'час'
    elif ch in q:
        ch1 = 'часа'
    elif ch in qq:
        ch1 = 'часов'
    else:
        ch1 = 'часов'

    q = [1,21,31,41,51]
    qq = [2,3,4,22,23,24,32,33,34,42,43,44,52,53,54]
    if mi in q:
        mi1 = 'минута'
    elif mi in qq:
        mi1 = 'минуты'
    else:
        mi1 = 'минут'

    if sek in q:
        sek1 = 'секунда'
    elif sek in qq:
        sek1 = 'секунды'
    else:
        sek1 = 'секунд'

    return ' '.join(['До Нового года',str(d),d1,str(ch),ch1,str(mi),mi1,str(sek),sek1])


bot = telebot.TeleBot('5844491437:AAHp0Ycgb8VuAHY-9WpG_r-u7RTzdGogFuw')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, taimer(), parse_mode='html')

bot.polling(none_stop=True)
