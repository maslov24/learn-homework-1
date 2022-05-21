"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import settings
import ephem
import datetime

logging.basicConfig(
    filename='bot.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S'
)

def date_is_today():    # format date for ephem
    d = datetime.date.today()
    date = (str(d.year) + '/' + str(d.month) + '/' + str(d.day))
    return date

def get_planet(user_planet):
    if user_planet == 'Mars':
        mars = ephem.Mars()
        mars.compute(date_is_today())
        return list(ephem.constellation(mars))[1]
    elif user_planet == 'Sun':
        sun = ephem.Sun()
        sun.compute(date_is_today())
        return list(ephem.constellation(sun))[1]
    elif user_planet == 'Moon':
        moon = ephem.Moon()
        moon.compute(date_is_today())
        return list(ephem.constellation(moon))[1]
    elif user_planet == 'Mercury':
        mercury = ephem.Mercury()
        mercury.compute(date_is_today())
        return list(ephem.constellation(mercury))[1]
    elif user_planet == 'Jupiter':
        jupiter = ephem.Jupiter()
        jupiter.compute(date_is_today())
        return list(ephem.constellation(jupiter))[1]
    elif user_planet == 'Venus':
        venus = ephem.Venus()
        venus.compute(date_is_today())
        return list(ephem.constellation(venus))[1]
    elif user_planet == 'Saturn':
        saturn = ephem.Saturn()
        saturn.compute(date_is_today())
        return list(ephem.constellation(saturn))[1]

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Приветствую, высокочтимый друг!')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def get_info_planet(update, context):
    user_planet = ' '.join(context.args)
    user_planet = user_planet.lower().strip().capitalize()
    planets = ['Mars', 'Sun', 'Moon', 'Mercury', 'Saturn', 'Venus', 'Jupiter']
    if user_planet in planets:
        update.message.reply_text(f'Планета {user_planet} сейчас расположена в созвездии {get_planet(user_planet)}')
    else:
        s= ', '.join(planets)
        update.message.reply_text(f'Планета не зарегистрирована в базе. Доступны следующие планеты: {s}')
def main():
    mybot = Updater(settings.API_KEY_TG, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_info_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал') 
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
    main()
