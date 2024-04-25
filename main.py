import calendar
from datetime import datetime
from urllib import response

import telebot
import webbrowser
import requests
#библиотека для погоды

import json
from telebot import types
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot('6641150738:AAEIL8jhbt7LWQaIP_wVJMspe1HlP1EW9Nc')
#токен API

API = '176598c0f0b2c81fc2f37b59a96e9ac5'

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com/?&hl=ru')
#функция открывает ваш сайт после этих запросов пользователя





@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Если у вас возникли трудности: '
                                     'позвоните нам по телефону 8 -777-777-77-77'
                                     ' или напишите нам на почту Rentacar@mail.ru '
                                     'и наши специалисты решат ваш вопрос')

@bot.message_handler(commands=['partner'])
def partner(message):
    bot.send_message(message.chat.id, '<b>покупайте какао</b> <em><U>Ван Гуттена</U></em>', parse_mode='html')




@bot.message_handler(commands=['start'])
def start(message):
    file = open('./Cars.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    # загрузка фото на команду в скобках
    bot.send_message(message.chat.id, f' {message.from_user.first_name}, ✅ Вас  приветствует официальный телеграмм бот, крупнейшей компании по прокату автомобилей по всему миру')
#функция обрабатывает команды(которые в скобках) и выводит данное собщение на них
#{message.from_user.first_name} это имя пользователя можно и другие данные
    bot.send_message(message.chat.id,f' {message.from_user.first_name},  <b>Введите город в каком вы хотите взять в аренду автомобиль</b>', parse_mode='html')
#второе сообщение вопрос про город



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
# отслеживает любой текст введеный пользователем

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    #ссылка для погоды подставляем переменную city
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp} градусов цельсия')
        bot.send_message(message.chat.id, f'Рекомендуемый тип автомобиля по погодным условиям')



        image = 'cabrio.jpg' if temp > 10.0 else 'sedan.jpg' or 'sedan.jpg' if temp > -5.0 else 'Hummer.jpg'
        file = open('./' + image, 'rb')

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('🚗 Автопарк', callback_data='auto'))
        markup.add(types.InlineKeyboardButton('📝 Условия аренды', callback_data='uslov'))
        markup.add(types.InlineKeyboardButton('🏆  Отзывы', callback_data='reviews'))
        bot.send_photo(message.chat.id, file, reply_markup=markup )
        #markup кнопка и передаем reply_markup=markup

    else:
        bot.reply_to(message, 'Город указан неверно')
        # проверка на неверно введеный город

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'auto':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('🚜 Эконом', callback_data='economy'))
        markup.add(types.InlineKeyboardButton('🚙 Комфорт', callback_data='comfort'))
        markup.add(types.InlineKeyboardButton('🚀  Бизнес', callback_data='business'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_message(callback.message.chat.id, f'🚗 Выберите класс автомобиля',reply_markup=markup)





    elif callback.data == 'uslov':
        file = open('./Dogovor.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ УСЛОВИЯ АРЕНДЫ'
                                                   f'\n🔹️ <b>Требования для арендатора</b>,'
                                                   f'\n- Наличие паспорта и водительских прав;'
                                                   f'\n- Стаж вождения от 3 лет;'
                                                   f'\n- Возраст от 25 лет;'
                                                   f'\n- Залог от 5000 рублей.'
                                                   f'\n🔹️ <b>Условия оплаты</b>'
                                                   f'\nОплатить аренду авто можно в момент передачи авто. '
                                                   f'\n🔹️ <b>Виды приема оплаты</b>'
                                                   f'\n- наличными в кассу;'
                                                   f'\n- картами Visa / MasterCard;'
                                                   f'\n- переводом на расчётный счёт;',  parse_mode='html',reply_markup=markup)



    elif callback.data == 'reviews':
        file = open('./reviews.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'Отзывы ⭐⭐⭐⭐⭐ \n\nЗдесь Вы можете прочитать отзывы клиентов о нашей работе '
                                                   f'\n\nyandex.ru'
                                                   f'\n2gis.ru'
                                                   f'\nvk.com'
                                                   f'\nweb.telegram.org'
                                                   f'\n\n\n😉 Если вы удовлетворены нашими услугами, нам будет очень приятно услышать от вас хорошие отзывы и пожелания!',reply_markup=markup)




    elif callback.data == 'economy':
        file = open('./kalina.jpeg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1⃣ ', callback_data='economy')
        btn2 = types.InlineKeyboardButton('2⃣', callback_data='two')
        btn3 = types.InlineKeyboardButton('3⃣', callback_data='three')
        markup.row(btn1, btn2,btn3)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ Lada kalina'
                                                   f' \nМеханика, Бензин, 1.6/78 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 1600 руб. '
                                                   f'\n2-3 сут. 1500 руб. '
                                                   f'\n4-7 сут. 1400 руб. '
                                                   f'\nОт 8 сут. 1300 руб. '
                                                   f'\nДепозит: 5000 руб.;', parse_mode='html', reply_markup=markup)

    elif callback.data == 'two':
        file = open('./matiz.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1⃣', callback_data='economy')
        btn2 = types.InlineKeyboardButton('2⃣', callback_data='two')
        btn3 = types.InlineKeyboardButton('3⃣', callback_data='three')
        markup.row(btn1, btn2,btn3)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ dewoo matiz'
                                                   f' \nМеханика, Бензин, 1.0/60 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 1400 руб. '
                                                   f'\n2-3 сут. 1200 руб. '
                                                   f'\n4-7 сут. 1100 руб. '
                                                   f'\nОт 8 сут. 1000 руб. '
                                                   f'\nДепозит: 4000 руб.;', parse_mode='html', reply_markup=markup)

    elif callback.data == 'three':
        file = open('./oka1.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1⃣', callback_data='economy')
        btn2 = types.InlineKeyboardButton('2⃣', callback_data='two')
        btn3 = types.InlineKeyboardButton('3⃣', callback_data='three')
        markup.row(btn1, btn2, btn3)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ Lada 1111(ОКА)'
                                                   f' \nМеханика, Бензин, 0.8/42 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 1000 руб. '
                                                   f'\n2-3 сут. 500 руб. '
                                                   f'\n4-7 сут. 400 руб. '
                                                   f'\nОт 8 сут. 300 руб. '
                                                   f'\nДепозит: 2000 руб.;', parse_mode='html', reply_markup=markup)


    elif callback.data == 'comfort':
        file = open('./solaris.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('1⃣ ', callback_data='comfort')
        btn5 = types.InlineKeyboardButton('2⃣', callback_data='four')
        btn6 = types.InlineKeyboardButton('3⃣', callback_data='five')
        markup.row(btn4, btn5, btn6)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ Hyundai Solaris'
                                                   f' \nАвтомат, Бензин, 1.6/123 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 3100 руб. '
                                                   f'\n2-3 сут. 3000 руб. '
                                                   f'\n4-7 сут. 2900 руб. '
                                                   f'\nОт 8 сут. 2800 руб. '
                                                   f'\nДепозит: 10000 руб.;', parse_mode='html', reply_markup=markup)

    elif callback.data == 'four':
        file = open('./Vesta.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('1⃣', callback_data='comfort')
        btn5 = types.InlineKeyboardButton('2⃣', callback_data='four')
        btn6 = types.InlineKeyboardButton('3⃣', callback_data='five')
        markup.row(btn4, btn5, btn6)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ Lada Vesta'
                                                   f' \nАвтомат, Бензин, 1.6/120 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 3400 руб. '
                                                   f'\n2-3 сут. 3200 руб. '
                                                   f'\n4-7 сут. 3100 руб. '
                                                   f'\nОт 8 сут. 3000 руб. '
                                                   f'\nДепозит: 14000 руб.;', parse_mode='html', reply_markup=markup)

    elif callback.data == 'five':
        file = open('./fiat.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('1⃣', callback_data='comfort')
        btn5 = types.InlineKeyboardButton('2⃣', callback_data='four')
        btn6 = types.InlineKeyboardButton('3⃣', callback_data='five')
        markup.row(btn4, btn5, btn6)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ Fiat egea'
                                                   f' \nМеханика, Бензин, 1.8/112 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 2500 руб. '
                                                   f'\n2-3 сут. 2000 руб. '
                                                   f'\n4-7 сут. 1500 руб. '
                                                   f'\nОт 8 сут. 1300 руб. '
                                                   f'\nДепозит: 9000 руб.;', parse_mode='html', reply_markup=markup)


    elif callback.data == 'business':
        file = open('./mersedes.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton('1⃣ ', callback_data='business')
        btn8 = types.InlineKeyboardButton('2⃣', callback_data='six')
        btn9 = types.InlineKeyboardButton('3⃣', callback_data='seven')
        markup.row(btn7, btn8, btn9)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ Mercedes-Benz'
                                                   f' \nАвтомат, Бензин, 2.0/211 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 8500 руб. '
                                                   f'\n2-3 сут. 8000 руб. '
                                                   f'\n4-7 сут. 7000 руб. '
                                                   f'\nОт 8 сут. 6000 руб. '
                                                   f'\nДепозит: 20000 руб.;', parse_mode='html', reply_markup=markup)

    elif callback.data == 'six':
        file = open('./Rolls.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton('1⃣ ', callback_data='business')
        btn8 = types.InlineKeyboardButton('2⃣', callback_data='six')
        btn9 = types.InlineKeyboardButton('3⃣', callback_data='seven')
        markup.row(btn7, btn8, btn9)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ rolls royce'
                                                   f' \nАвтомат, Бензин, 5.0/511 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 14000 руб. '
                                                   f'\n2-3 сут. 12000 руб. '
                                                   f'\n4-7 сут. 11000 руб. '
                                                   f'\nОт 8 сут. 10000 руб. '
                                                   f'\nДепозит: 40000 руб.;', parse_mode='html', reply_markup=markup)

    elif callback.data == 'seven':
        file = open('./BMW.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton('1⃣ ', callback_data='business')
        btn8 = types.InlineKeyboardButton('2⃣', callback_data='six')
        btn9 = types.InlineKeyboardButton('3⃣', callback_data='seven')
        markup.row(btn7, btn8, btn9)
        markup.add(types.InlineKeyboardButton('🔍Выбрать даты', callback_data='calendar'))
        markup.add(types.InlineKeyboardButton('⭐Главное меню', callback_data='back'))
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, f'🛡️ BMW'
                                                   f' \nАвтомат, Бензин, 3.0/311 л.с. '
                                                   f'\nЦены с 1 января - 30 апреля '
                                                   f'\n1 сут. 10000 руб. '
                                                   f'\n2-3 сут. 5000 руб. '
                                                   f'\n4-7 сут. 4000 руб. '
                                                   f'\nОт 8 сут. 3000 руб. '
                                                   f'\nДепозит: 20000 руб.;', parse_mode='html', reply_markup=markup)



    elif callback.data == 'calendar':
        dates = [datetime.now()]
        markup = types.InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(date.strftime('%d.%m.%Y'),callback_data=date.strftime('%d.%m.%Y')) for date in dates]
        for i in range(0, len(buttons), 3):
            markup.add(*buttons[i:i + 3])
        markup.add(types.InlineKeyboardButton('Подтвердить бронирование', callback_data='yes'))
        bot.send_message(callback.message.chat.id,text="Список свободных дат:",reply_markup=markup)

    elif callback.data == 'yes':
        markup = types.InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id, f'Бронирование подтверждено, оставайтесь на месте машину привезут к вам в течении 5 мин', reply_markup=markup)






    elif callback.data == 'back':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('                            🚗 Автопарк                          ', callback_data='auto'))
        markup.add(types.InlineKeyboardButton('                           📝 Условия аренды                     ', callback_data='uslov'))
        markup.add(types.InlineKeyboardButton('                            🏆 Отзывы                            ', callback_data='reviews'))
        bot.send_message(callback.message.chat.id, f'.                   Главное меню                  .',reply_markup=markup)
# отслеживают ввод кнопок









@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id} ')
#функция отвечает на сообщение введеное пользователем (в скобках ключевые слова)





if __name__ == "__main__":
    bot.polling(none_stop=True)
# застовляет работать программу постоянно (не завершаясь)