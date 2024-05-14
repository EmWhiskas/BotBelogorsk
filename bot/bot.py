import random
import shutil
import os
import subprocess
import telebot
from telebot import types
import ZaprosAlleys, ZaprosParki, ZaprosSquares, ZaprosMonuments, ZaprosFacts, ZaprosCulture
bot = telebot.TeleBot('6909012923:AAHsP4syZ6iEwjWUFnrqukP0JzFzKqx2vKk')
parks = False
alleys = False
squares = False
monuments = False
cultura = False
update = False


#Путь к боту
waytobot = r'C:\\Users\\Максим\\PycharmProjects\\BotBelogorsk\\bot\\updater.py'
#^^^^^^^^^^^^


rangParks = ['Информация!H4:H7', 'Информация!K4:K7', 'Информация!N4:N7']
rangAlleys = ['Информация!H11:H12', 'Информация!K11:K12']
rangSquares = ['Информация!H18:H20', 'Информация!K18:K20', 'Информация!N18:N20', 'Информация!Q18:Q20']
rangMonuments = ['Информация!H26:H28', 'Информация!K26:K28', 'Информация!N26:N28', 'Информация!Q26:Q28', 'Информация!T26:T28', 'Информация!W26:W28', 'Информация!Z26:Z28', 'Информация!AC26:AC28', 'Информация!AF26:AF28']
rangFacts = ['Информация!G47:G48', 'Информация!H47:H48', 'Информация!I47:I48', 'Информация!J47:J48']
places = [rangParks, rangAlleys, rangSquares, rangMonuments]

def handle_docs(msg):
    try:
        # Создаем папку, если она еще не существует
        new_folder = 'апдейты'
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # Получаем файл
        file_info = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Имя файла для сохранения
        save_filename = 'file_0.py'

        # Сохраняем файл в новую папку с именем file_0
        with open(os.path.join(new_folder, save_filename), 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(msg, "Файл успешно скопирован под именем file_0!")
        filename = waytobot
        subprocess.run(['python', filename])
        bot.stop_bot()

    except Exception as e:
        bot.reply_to(msg, e)

def infoparks(msg, rang):
    bot.send_chat_action(msg.chat.id, 'typing')
    ZaprosParki.clear()
    res = ZaprosParki.main(rang)
    for i in res[0]:
        ans = '\n'.join(res[0])

    photos = res[1]
    photos = ''.join(photos)
    try:
        photos.replace('\n', '')
    except:
        pass
    photos = photos.split()
    for one in photos:
        if one == ' Следующее ':
            photos.remove(one)
        else:
            pass

    print(res)
    def send_photos_with_text(chat_id, photos, ans):
        medias = []
        for link in photos:
            # Добавляем каждую фотографию с текстовой подписью
            medias.append(telebot.types.InputMediaPhoto(link))
        # Отправляем группу медиа-объектов как одно сообщение
        bot.send_media_group(chat_id, medias)
        bot.send_message(chat_id, ans, parse_mode='HTML')
    bot.send_chat_action(msg.chat.id, 'cancel')
    send_photos_with_text(msg.chat.id, photos, ans)
    keys(msg)

def infoalleys(msg, rang):
    bot.send_chat_action(msg.chat.id, 'typing')
    ZaprosAlleys.clear()

    res = ZaprosAlleys.main(rang)
    for i in res[0]:
        ans = '\n'.join(res[0])

    photos = res[1]
    photos = ''.join(photos)
    try:
        photos.replace('\n', '')
    except:
        pass
    photos = photos.split()
    for one in photos:
        if one == 'Следующее':
            photos.remove(one)
        else:
            pass

    print(res)
    def send_photos_with_text(chat_id, photos, ans):
        medias = []
        for link in photos:
            # Добавляем каждую фотографию с текстовой подписью
            medias.append(telebot.types.InputMediaPhoto(link))
        # Отправляем группу медиа-объектов как одно сообщение
        bot.send_media_group(chat_id, medias)
        bot.send_message(chat_id, ans, parse_mode='HTML')
    bot.send_chat_action(msg.chat.id, 'cancel')
    send_photos_with_text(msg.chat.id, photos, ans)
    keys(msg)

def infosquares(msg, rang):
    bot.send_chat_action(msg.chat.id, 'typing')
    ZaprosSquares.clear()

    res = ZaprosSquares.main(rang)
    for i in res[0]:
        ans = '\n'.join(res[0])

    photos = res[1]
    photos = ''.join(photos)
    try:
        photos.replace('\n', '')
    except:
        pass
    photos = photos.split()
    for one in photos:
        if one == 'Следующее':
            photos.remove(one)
        else:
            pass

    print(res)
    def send_photos_with_text(chat_id, photos, ans):
        medias = []
        for link in photos:
            # Добавляем каждую фотографию с текстовой подписью
            medias.append(telebot.types.InputMediaPhoto(link))
        # Отправляем группу медиа-объектов как одно сообщение
        bot.send_media_group(chat_id, medias)
        bot.send_message(chat_id, ans, parse_mode='HTML')
    bot.send_chat_action(msg.chat.id, 'cancel')
    send_photos_with_text(msg.chat.id, photos, ans)
    keys(msg)

def infomonuments(msg, rang):
    bot.send_chat_action(msg.chat.id, 'typing')
    ZaprosMonuments.clear()

    res = ZaprosMonuments.main(rang)
    for i in res[0]:
        ans = '\n'.join(res[0])

    photos = res[1]
    photos = ''.join(photos)
    try:
        photos.replace('\n', '')
    except:
        pass
    photos = photos.split()
    for one in photos:
        if one == ' Следующее ':
            photos.remove(one)
        else:
            pass

    print(res)
    def send_photos_with_text(chat_id, photos, ans):
        medias = []
        for link in photos:
            # Добавляем каждую фотографию с текстовой подписью
            medias.append(telebot.types.InputMediaPhoto(link))
            print(medias)
        # Отправляем группу медиа-объектов как одно сообщение
        bot.send_media_group(chat_id, medias)
        bot.send_message(chat_id, ans, parse_mode='HTML')
    bot.send_chat_action(msg.chat.id, 'cancel')
    send_photos_with_text(msg.chat.id, photos, ans)
    keys(msg)

def randPlace(msg):
    typ = random.choice(places)
    place = random.choice(typ)
    if typ == rangParks:
        bot.send_message(msg.chat.id, 'Пойдем в парк')
        infoparks(msg, place)
    elif typ == rangAlleys:
        bot.send_message(msg.chat.id, 'Прогуляйся по аллеям')
        infoalleys(msg, place)
    elif typ == rangSquares:
        bot.send_message(msg.chat.id, 'Нашел интересный сквер')
        infosquares(msg, place)
    elif typ == rangMonuments:
        bot.send_message(msg.chat.id, 'Обязательно сходи к этому памятнику')
        infomonuments(msg, place)

def facts(msg, rang):
    ZaprosFacts.clear()
    res = ZaprosFacts.main(rang)
    ans = '\n'.join(res)
    bot.send_message(msg.chat.id, ans, parse_mode='HTML')

def infoсultura(msg, rang):
    bot.send_chat_action(msg.chat.id, 'typing')
    ZaprosCulture.clear()

    res = ZaprosCulture.main(rang)
    for i in res[0]:
        ans = '\n'.join(res[0])

    photos = res[1]
    photos = ''.join(photos)
    try:
        photos.replace('\n', '')
    except:
        pass
    photos = photos.split()
    for one in photos:
        if one == ' Следующее ':
            photos.remove(one)
        else:
            pass

    print(res)

    def send_photos_with_text(chat_id, photos, ans):
        medias = []
        for link in photos:
            # Добавляем каждую фотографию с текстовой подписью
            medias.append(telebot.types.InputMediaPhoto(link))
            print(medias)
        # Отправляем группу медиа-объектов как одно сообщение
        bot.send_media_group(chat_id, medias)
        bot.send_message(chat_id, ans, parse_mode='HTML')
    bot.send_chat_action(msg.chat.id, 'cancel')
    send_photos_with_text(msg.chat.id, photos, ans)
    keys(msg)
@bot.message_handler(commands=['start', 'help'])
def start(info):
    kb = types.ReplyKeyboardMarkup(row_width=2)
    but1 = types.KeyboardButton('Парки')
    but2 = types.KeyboardButton('Аллеи')
    but3 = types.KeyboardButton('Скверы')
    but4 = types.KeyboardButton('Памятники')
    but5 = types.KeyboardButton('Хочу окультуриться 👨‍🎓')
    # but6 = types.KeyboardButton('Где можно прогуляться?🏃‍♀️')
    but7 = types.KeyboardButton('Выбери за меня, куда пойти🤸‍♀️')
    but8 = types.KeyboardButton('Интересные факты о городе ⛺')

    kb.add(but1, but2, but3, but4, but5, but7, but8)
    bot.send_message(info.chat.id, 'Привет', reply_markup = kb)

def keys(msg):
    global parks, alleys, squares, monuments
    kb = types.ReplyKeyboardMarkup(row_width=2)
    but1 = types.KeyboardButton('Парки')
    but2 = types.KeyboardButton('Аллеи')
    but3 = types.KeyboardButton('Скверы')
    but4 = types.KeyboardButton('Памятники')
    but5 = types.KeyboardButton('Хочу окультуриться 👨‍🎓')
    # but6 = types.KeyboardButton('Где можно прогуляться?🏃‍♀️')
    but7 = types.KeyboardButton('Выбери за меня, куда пойти🤸‍♀️')
    but8 = types.KeyboardButton('Интересные факты о городе ⛺')
    kb.add(but1, but2, but3, but4, but5, but7, but8)
    parks = False
    alleys = False
    squares = False
    monuments = False
    bot.send_message(msg.chat.id, 'Рад был помочь', reply_markup=kb)

def parki(msg):
    global parks
    parks = True
    kb = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('Городской парк культуры и отдыха')
    but2 = types.KeyboardButton('Парк имени Дзержинского')
    but3 = types.KeyboardButton('Парк Амурсельмаш')

    kb.add(but1, but2, but3)
    bot.send_message(msg.chat.id, 'Какой парк тебя интересует', reply_markup=kb)

def alleyskeys(msg):
    global alleys
    alleys = True
    kb = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('Аллея молодежи')
    but2 = types.KeyboardButton('Аллея Героев Славы	')

    kb.add(but1, but2,)
    bot.send_message(msg.chat.id, 'Выбирай', reply_markup=kb)

def squareskeys(msg):
    global squares
    squares = True
    kb = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('Жемчужина')
    but2 = types.KeyboardButton('Молодежный')
    but3 = types.KeyboardButton('Чеховский')
    but4 = types.KeyboardButton('Александровский')
    kb.add(but1, but2, but3, but4)
    bot.send_message(msg.chat.id, 'О каком сквере поговорим?', reply_markup=kb)

def monumentskeys(msg):
    global monuments
    monuments = True
    kb = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('Памятник "Ротану"')
    but2 = types.KeyboardButton('Монументы В.И. Ленину')
    # but3 = types.KeyboardButton('Братская могила 312 борцам')
    but4 = types.KeyboardButton('Памятник вежливому солдату')
    but5 = types.KeyboardButton('Обелиск «Героям-комсомольцам»')
    but6 = types.KeyboardButton('Памятник Телега переселенцев')
    but7 = types.KeyboardButton('Памятник «Паровоз-П36»')
    but8 = types.KeyboardButton('Камень «Памяти жертв политических репрессий»')
    but9 = types.KeyboardButton('Памятник Воину-освободителю')
    kb.add(but1, but2, but4, but5, but6, but7, but8, but9)
    bot.send_message(msg.chat.id, 'Куда на этот раз?', reply_markup=kb)

def culturakeys(msg):
    global cultura
    cultura = True
    kb = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('Детская школа искусств')
    but2 = types.KeyboardButton('Центр культурного развития')
    but3 = types.KeyboardButton('Дом культуры "Амурсельмаш"')
    but4 = types.KeyboardButton('Центральная библиотечная система им. Максима Горького')
    kb.add(but1, but2, but3, but4)
    bot.send_message(msg.chat.id, 'Выбери учреждение культуры, которое ты хочешь посетить', reply_markup=kb)

@bot.message_handler(content_types=['photo'])
def photo(msg):
    print(msg)

@bot.message_handler(content_types=['text'])
def message(msg):
    msg.text = msg.text.lower()
    print(msg.chat.id, msg.text)
    if 'парки' in msg.text:
        parki(msg)

    elif msg.text == 'городской парк культуры и отдыха' and parks == True:
        rang = 'Информация!H4:H7'
        infoparks(msg, rang)

    elif msg.text == 'парк имени дзержинского' and parks == True:
        rang = 'Информация!K4:K7'
        infoparks(msg, rang)

    elif msg.text == 'парк амурсельмаш' and parks == True:
        rang = 'Информация!N4:N7'
        infoparks(msg, rang)

    elif 'аллеи' in msg.text:
        alleyskeys(msg)
        
    elif msg.text == 'аллея молодежи' and alleys == True:
        rang = 'Информация!H11:H12'
        infoalleys(msg, rang)

    elif msg.text == 'аллея героев славы' and alleys == True:
        rang = 'Информация!K11:K12'
        infoalleys(msg, rang)

    elif 'скверы' in msg.text:
        squareskeys(msg)

    elif msg.text == 'жемчужина' and squares == True:
        rang = 'Информация!H18:H20'
        infosquares(msg, rang)

    elif msg.text == 'молодежный' and squares == True:
        rang = 'Информация!K18:K20'
        infosquares(msg, rang)

    elif msg.text == 'чеховский' and squares == True:
        rang = 'Информация!N18:N20'
        infosquares(msg, rang)

    elif msg.text == 'александровский' and squares == True:
        rang = 'Информация!Q18:Q20'
        infosquares(msg, rang)

    elif 'памятники' in msg.text:
        monumentskeys(msg)

    elif msg.text == 'памятник "ротану"' and monuments == True:
        rang = 'Информация!H26:H28'
        infomonuments(msg, rang)

    elif msg.text == 'монументы в.и. ленину' and monuments == True:
        rang = 'Информация!K26:K28'
        infomonuments(msg, rang)

    elif msg.text == 'памятник святым супругам петру и февронии.' and monuments == True:
        rang = 'Информация!N26:N28'
        infomonuments(msg, rang)

    elif msg.text == 'памятник вежливому солдату' and monuments == True:
        rang = 'Информация!Q26:Q28'
        infomonuments(msg, rang)

    elif msg.text == 'обелиск «героям-комсомольцам»' and monuments == True:
        rang = 'Информация!T26:T28'
        infomonuments(msg, rang)

    elif msg.text == 'памятник телега переселенцев' and monuments == True:
        rang = 'Информация!W26:W28'
        infomonuments(msg, rang)

    elif msg.text == 'памятник «паровоз-п36»' and monuments == True:
        rang = 'Информация!Z26:Z28'
        infomonuments(msg, rang)

    elif msg.text == 'камень «памяти жертв политических репрессий»' and monuments == True:
        rang = 'Информация!AC26:AC28'
        infomonuments(msg, rang)

    elif msg.text == 'памятник воину-освободителю' and monuments == True:
        rang = 'Информация!AF26:AF28'
        infomonuments(msg, rang)

    elif 'выбери за меня, куда пойти🤸‍♀️' in msg.text:
        randPlace(msg)

    elif 'интересные факты о городе ⛺' in msg.text:
        rang = random.choice(rangFacts)
        facts(msg, rang)

    elif 'хочу окультуриться 👨‍🎓' in msg.text:
        culturakeys(msg)

    elif msg.text == 'детская школа искусств' and cultura == True:
        rang = 'Информация!H53:H55'
        infoсultura(msg, rang)

    elif msg.text == 'центр культурного развития' and cultura == True:
        rang = 'Информация!I53:I55'
        infoсultura(msg, rang)

    elif msg.text == 'дом культуры "амурсельмаш"' and cultura == True:
        rang = 'Информация!J53:J55'
        infoсultura(msg, rang)

    elif msg.text == 'центральная библиотечная система им. максима горького' and cultura == True:
        rang = 'Информация!K53:K55'
        infoсultura(msg, rang)

    else:
        bot.send_message(msg.chat.id, 'Не распознал сообщение')
        start(msg)

@bot.message_handler(content_types=['document'])
def file(msg):
    print(msg)
    handle_docs(msg)

bot.infinity_polling()