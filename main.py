
from string import Template
import telebot
from telebot import types
TOKEN = '5268022321:AAGRXcBAWkbGrTvrOjYgr64tFW_Whuxc4OQ'
bot = telebot.TeleBot(TOKEN)
bot.delete_webhook()
CHAT_ID = '-1001533115482'
user_dict = {}


class User:
    def __init__(self, city):
        self.city = city
        keys = ['invest', 'invest_cash', 'invest_cash_reg', 'mortgage_reg', 'mortgage', 'driveN', 'driveR', 'driveS', 'driveV',
                'driveL', 'driveG', 'driveF', 'driveD', 'driveA', 'driveZ', 'driveI', 'driveP', 'driveX', 'driveM',
                'driveQ', 'driveJ', 'driveMM', 'driveE', 'driveY', 'driveO', 'driveH']
        for key in keys:
            self.key = None


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    inv = types.KeyboardButton('/Инвестиции')
    sell = types.KeyboardButton('/Продажа')
    pay = types.KeyboardButton('/Покупка')
    markup.add(inv, sell, pay)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}, я бот и ты можешь выбрать следующие действия !'.format(message.from_user), reply_markup=markup)








@bot.message_handler(commands=['Инвестиции'])
def bot_message(message):
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        user = user_dict[chat_id]
        user.invest = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cash = types.KeyboardButton('Наличные')
        mortgage = types.KeyboardButton('Ипотека')
        back = types.KeyboardButton('Назад')
        markup.add(cash, mortgage, back)
        msg = bot.send_message(chat_id, 'Продолжим', reply_markup=markup)
        bot.register_next_step_handler(msg, process_person_step)
        bot.register_next_step_handler(msg, process_person_step1)
        bot.register_next_step_handler(msg, return_step)

def process_person_step(message):
    if message.text == 'Наличные':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.invest_cash = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, 'Введите сумму и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: 40000000;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg, func1)
def func1(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.invest_cash_reg = message.text
        bot.send_message(chat_id,  'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData(user, 'Заявка от бота', bot.get_me().username, message.from_user.first_name), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')


def getRegData(user, title, name, name_user):
    t = Template('$title *$name* \n Имя: *$name_user* \n Выбор пункта 1: *$invest* \n Выбор пункта 2: *$invest_cash* \n Данные : *$invest_cash_reg*')
    return t.substitute({
        'title': title,
        'name': name,
        'name_user': name_user,
        'invest': user.invest,
        'invest_cash': user.invest_cash,
        'invest_cash_reg': user.invest_cash_reg
    })

def process_person_step1(message):
    if message.text == 'Ипотека':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.mortgage = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg1 = bot.send_message(chat_id, 'Введите сумму, первоначальный взнос, комфортный платеж и ваш контактный номер, чтобы мы могли взязаться с вами :(Пример: 40000000;1000000;15000;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg1, func2)
def func2(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.mortgage_reg = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData1(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')

def return_step(message):
    if message.text == 'Назад':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton('/Инвестиции')
        two = types.KeyboardButton('/Продажа')
        three = types.KeyboardButton('/Покупка')
        markup.add(one, two, three)
        bot.send_message(chat_id, 'Хорошо, давайте начнем заново'.format(message.from_user), reply_markup=markup)
def getRegData1(user, title, name):
    s = Template('$title *$name* \n Выбор пункта 1: *$invest* \n Выбор пункта 2: *$mortgage* \n Данные : *$mortgage_reg*')
    return s.substitute({
        'title': title,
        'name': name,
        'invest': user.invest,
        'mortgage': user.mortgage,
        'mortgage_reg': user.mortgage_reg
    })


@bot.message_handler(commands=['Покупка'])
def bot_message2(message):
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        user = user_dict[chat_id]
        user.driveN = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vt = types.KeyboardButton('Вторичка')
        nv = types.KeyboardButton('Новостройка')
        bc = types.KeyboardButton('Назад')
        markup.add(vt, nv, bc)
        msg3 = bot.send_message(chat_id, 'Продолжим', reply_markup=markup)
        bot.register_next_step_handler(msg3, process_city_step2)
        bot.register_next_step_handler(msg3, process_city_step3)
        bot.register_next_step_handler(msg3, back2)

def process_city_step2(message):
    if message.text == 'Вторичка':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveS = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vt = types.KeyboardButton('Ипотека')
        nv = types.KeyboardButton('Наличные')
        bc1 = types.KeyboardButton('Назад')
        markup.add(vt, nv, bc1)
        msg4 = bot.send_message(chat_id, 'Продолжим', reply_markup=markup)
        bot.register_next_step_handler(msg4, process_city_step4)
        bot.register_next_step_handler(msg4, process_city_step5)
        bot.register_next_step_handler(msg4, back2)
def process_city_step3(message):
    if message.text == 'Новостройка':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveL = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vt1 = types.KeyboardButton('Ипотека')
        nv1 = types.KeyboardButton('Наличные')
        bc2 = types.KeyboardButton('Назад')
        markup.add(vt1, nv1, bc2)
        msg5 = bot.send_message(chat_id, 'Продолжим', reply_markup=markup)
        bot.register_next_step_handler(msg5, process_city_step6)
        bot.register_next_step_handler(msg5, process_city_step7)
        bot.register_next_step_handler(msg5, back2)
def process_city_step4(message):
    if message.text == 'Ипотека':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveV = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg1 = bot.send_message(chat_id, 'Введите сумму, первоначальный взнос, комфортный платеж и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: 40000000;1000000;15000;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg1, func3)
def process_city_step5(message):
    if message.text == 'Наличные':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveF = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg1 = bot.send_message(chat_id, 'Введите сумму и комфортный платеж и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: 40000000;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg1, func4)
def func3(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveD = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData2(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')

def func4(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveZ = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData3(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')

def getRegData3(user, title, name):
    f = Template('$title *$name* \n Выбор пункта 1: *$driveN* \n Выбор пункта 2: *$driveS* \n Выбор пункта 3: *$driveF* \n Данные: *$driveZ* ')
    return f.substitute({
        'title': title,
        'name': name,
        'driveN': user.driveN,
        'driveS':user.driveS,
        'driveF': user.driveF,
        'driveZ': user.driveZ
    })
def getRegData2(user, title, name):
    s = Template('$title *$name* \n Выбор пункта 1: *$driveN* \n Выбор пункта 2: *$driveS* \n Выбор пункта 3: *$driveV* \n Данные: *$driveD* ')
    return s.substitute({
        'title': title,
        'name': name,
        'driveN': user.driveN,
        'driveS':user.driveS,
        'driveV': user.driveV,
        'driveD': user.driveD
    })

def process_city_step6(message):
    if message.text == 'Ипотека':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveG = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg1 = bot.send_message(chat_id, 'Введите сумму, первоначальный взнос, комфортный платеж и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: 40000000;1000000;15000;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg1, func5)
def process_city_step7(message):
    if message.text == 'Наличные':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveA = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg1 = bot.send_message(chat_id, 'Введите сумму и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: 40000000;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg1, func6)

def func5(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveP = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData5(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')
def func6(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveI = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData6(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')

def back2(message):
    if message.text == 'Назад':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton('/Инвестиции')
        two = types.KeyboardButton('/Продажа')
        three = types.KeyboardButton('/Покупка')

        markup.add(one, two, three)
        bot.send_message(chat_id, 'Хорошо, давайте начнем заново'.format(message.from_user), reply_markup=markup)

def getRegData5(user, title, name):
    f = Template('$title *$name* \n Выбор пункта 1: *$driveN* \n Выбор пункта 2: *$driveL* \n Выбор пункта 3: *$driveG* \n Данные: *$driveP* ')
    return f.substitute({
        'title': title,
        'name': name,
        'driveN': user.driveN,
        'driveL': user.driveL,
        'driveG': user.driveG,
        'driveP': user.driveP
    })
def getRegData6(user, title, name):
    f = Template('$title *$name* \n Выбор пункта 1: *$driveN* \n Выбор пункта 2: *$driveL* \n Выбор пункта 3: *$driveA* \n Данные: *$driveI* ')
    return f.substitute({
        'title': title,
        'name': name,
        'driveN': user.driveN,
        'driveL': user.driveL,
        'driveA': user.driveA,
        'driveI': user.driveI
    })

@bot.message_handler(commands=['Продажа'])
def bot_message3(message):
    chat_id = message.chat.id
    user_dict[chat_id] = User(message.text)
    user = user_dict[chat_id]
    user.driveX = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vt2 = types.KeyboardButton('Обмен')
    nv2 = types.KeyboardButton('Оценка')
    bc2 = types.KeyboardButton('Назад')
    markup.add(vt2, nv2, bc2)
    msg6 = bot.send_message(chat_id, 'Продолжим', reply_markup=markup)
    bot.register_next_step_handler(msg6, process_city_step8)
    bot.register_next_step_handler(msg6, process_city_step9)
    bot.register_next_step_handler(msg6, back3)

def process_city_step8(message):
    if message.text == 'Обмен':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveM = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vt3 = types.KeyboardButton('Вторичка')
        nv3 = types.KeyboardButton('Новостройка')
        bc3 = types.KeyboardButton('Назад')
        markup.add(vt3, nv3, bc3)
        msg7 = bot.send_message(chat_id, 'Продолжим', reply_markup=markup)
        bot.register_next_step_handler(msg7, process_city_step10)
        bot.register_next_step_handler(msg7, process_city_step11)
        bot.register_next_step_handler(msg7, back3)
def process_city_step10(message):
    if message.text == 'Вторичка':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveJ = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg8 = bot.send_message(chat_id, 'Введите адрес, площадь в м2 и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: НСК, красный проспект 1; 100м2;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg8, func7)
def process_city_step11(message):
    if message.text == 'Новостройка':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveMM = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg9 = bot.send_message(chat_id, 'Введите адрес, площадь в м2 и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: НСК, красный проспект 1; 100м2;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg9, func8)

def func7(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveE = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData7(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')
def func8(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveY = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData8(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')

def getRegData7(user, title, name):
    u = Template('$title *$name* \n Выбор пункта 1: *$driveX* \n Выбор пункта 2: *$driveM* \n Выбор пункта 3: *$driveJ* \n Данные: *$driveE* ')
    return u.substitute({
        'title': title,
        'name': name,
        'driveX': user.driveX,
        'driveM': user.driveM,
        'driveJ': user.driveJ,
        'driveE': user.driveE
    })
def getRegData8(user, title, name):
    i = Template('$title *$name* \n Выбор пункта 1: *$driveX* \n Выбор пункта 2: *$driveM* \n Выбор пункта 3: *$driveMM* \n Данные: *$driveY* ')
    return i.substitute({
        'title': title,
        'name': name,
        'driveX': user.driveX,
        'driveM': user.driveM,
        'driveMM': user.driveMM,
        'driveY': user.driveY
    })
def process_city_step9(message):
    if message.text == 'Оценка':
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveO = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg10 = bot.send_message(chat_id, 'Введите адрес, площадь в м2 и ваш контактный номер, чтобы мы могли взязаться с вами:(Пример: НСК, красный проспект 1; 100м2;79...)', reply_markup=markup)
        bot.register_next_step_handler(msg10, func9)
def func9(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driveH = message.text
        bot.send_message(chat_id, 'Ваша заявка принята! Наш специалист скоро свяжется с вами 😊', parse_mode='Markdown')
        bot.send_message(CHAT_ID, getRegData9(user, 'Заявка от бота', bot.get_me().username), parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, 'ooops')
def back3(message):
    if message.text == 'Назад':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton('/Инвестиции')
        two = types.KeyboardButton('/Продажа')
        three = types.KeyboardButton('/Покупка')

        markup.add(one, two, three)
        bot.send_message(chat_id, 'Хорошо, давайте начнем заново'.format(message.from_user), reply_markup=markup)
def getRegData9(user, title, name):
    p = Template('$title *$name* \n Выбор пункта 1: *$driveX*  \n Выбор пункта 2: *$driveO* \n Данные: *$driveH* ')
    return p.substitute({
        'title': title,
        'name': name,
        'driveX': user.driveX,
        'driveO': user.driveO,
        'driveH': user.driveH
    })
bot.polling(none_stop=True)
