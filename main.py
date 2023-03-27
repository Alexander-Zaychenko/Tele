import requests
import random
from bs4 import BeautifulSoup as bs
import telebot
from games.rock_scissors_paper import in_game, engine, engine_hard
from playsound import playsound
from datetime import datetime
import keyboard

print(str(datetime.now())[:19])
URL1 = 'https://www.anekdotovmir.ru/anekdoty-bez-mata-i-plohih-slov/'
URL2 = 'https://anekdotbar.ru/'
URL3 = 'https://yandex.ru/pogoda/'
API_KEY = '6059936220:AAF4VS47NQp0kl88pqVlefTbhKzva-eVv_o'
uses = [[(5540433388, 'readed joke 1-9', '2023-03-25 11:39:51'), (5540433388, 'readed joke 10-19', '2023-03-25 11:39:58'), (5540433388, 'calculate', '2023-03-25 11:40:21'), (5540433388, 'wanted word', '2023-03-25 11:40:59'), (5540433388, 'played rsph', '2023-03-25 11:41:16')]]


def parser_anekdot_ru(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='entry-content clr')
    return [c.text for c in anekdots]


def parser_anekdotovstreet(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='tecst')
    return [c.text for c in anekdots]


def parser_weather(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    weather = soup.find_all('class', class_='temp__value temp__value_with-unit')
    print(weather)
    return weather
    # return [c.text for c in weather]


jokes = [
    'В супермаркете супружеская пара подкатывает с двумя набитыми тележками к кассе. Жена:\n'
    '— Ой забыли туалетную бумагу взять.\n'
    'Муж:\n'
    '— Не надо, у нас чек 60 метров будет.', 'Жена:\n'
                                             '— Мне нужны внимание и уход!\n'
                                             'Муж:\n'
                                             '— Внимание… я ухожу.',
    '— Да я ведь все сам!!! Все своими руками… Дом построил, сам! Вот этими вот руками. Сад посадил сам, своими руками, машину отремонтировал… Все САМ!!! Все своими руками...'
    '— Да, ты небось и не женат.'
    '— Нет, все сам, все своими руками...',
    '— Алло! Это психиатрическая клиника? Моя хозяйка думает, что у неё говорящий кот! Да, выезжайте скорее!',
    '— Опа! Леша пришел. Теперь мы можем заняться любимым делом.'
    '— Каким?'
    '— Ждать пока Леша уйдет.',
    'Мои соседи слушают офигенные песни, и мне все равно, хотят они этого или нет.',
    '— Маша, а давай уже по взрослому?!'
    '— Давай, Петя.'
    '— Мария Петровна!!!'
    '— Петр Сергеевич!!!',
    'Очень полная женщина, желая похудеть, повесила у себя в кухне памятку:'
    '«Я не ем после шести». Муж дописал: «УТРА!!!».',
    '— Скажите, в чём разница между этим и этим телефонами?'
    '— Разница между этим и этим телефонами в том что вот это MP3-плеер, а это — фотоаппарат...',
]
list_of_jokes = jokes
random.shuffle(list_of_jokes)
list_of_jokes2 = parser_anekdotovstreet(URL2)
random.shuffle(list_of_jokes2)
weather = [parser_weather(URL3)]

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(
        message.chat.id,
        'Привет, напиши мне любую цифру от 1 до 19, а я тебе пришлю анекдот: ')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(
        message.chat.id,
        "Бот, который присылает анекдоты при написании цифры\n"
        "Все совпадения случайны, может присутствовать ненормативная лексика, "
        "все анекдоты взяты с сайтов: https://www.anekdot.ru/release/anekdot/week/, "
        "https://anekdotbar.ru/\nБот создан 21.02.2023 Александром\nконтакты: +7(915)"
        "135 33-05,\nalexzay2012@yandex.ru\nработает с 9:00 до 21:00"

        "Игры: кнб (1-3) - Камень Ножницы бумага 1 - камень, 2 - ножницы, 3 - бумага  "
        "")


@bot.message_handler(commands=['weather'])
def weather(message):
    try:
        bot.send_message(message.chat.id, list(weather))
    except:
        bot.send_message(message.chat.id, "Error! This function in the deveopment")


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.lower() in '123456789':
        if len(list_of_jokes) > 0:
            print(f'{message.chat.id} readed joke {list_of_jokes[0]}')
            uses.append((message.chat.id, 'readed joke 1-9', str(datetime.now())[:19]))
            bot.send_message(message.chat.id, f'{list_of_jokes[0]}')
            del list_of_jokes[0]
        else:
            bot.send_message(message.chat.id, 'Try numbers 10-19')
    elif message.text.lower() in '111213141516171819':
        bot.send_message(message.chat.id, list_of_jokes2[0])
        uses.append((message.chat.id, 'readed joke 10-19', str(datetime.now())[:19]))
        print(f'{message.chat.id} readed joke {list_of_jokes2[0]}')
        del list_of_jokes2[0]
    elif message.text[0:4].lower() == 'кнбс':
        computer_choice = random.randint(1, 10)
        result = engine_hard(computer_choice, int(message.text[5]))
        bot.send_message(message.chat.id, result)
        print(f'{message.chat.id}, с результатом {result}')
        uses.append((message.chat.id, 'played rsph', str(datetime.now())[:19])) # rsph - rock scissors paper hard
    elif message.text[0:4].lower() == 'кнб':
        if not message.chat.id == 1323115182:
            result = in_game(message.text[4:len(message.text)])
            bot.send_message(message.chat.id, f'{result}')
            print(f'{message.chat.id}, с результатом {result}')
        else:
            computer_choice = random.randint(1, 100)
            if computer_choice != 1:
                bot.send_message(message.chat.id, "Победа! ")
                uses.append(("Mother", 'played rsp', str(datetime.now())[:19]))
                print("Mother always win! ")
            else:
                bot.send_message(message.chat.id, 'Поражение')
                print('Mother lose!!!!!')
    elif message.text[0:4].lower() == 'калк':
        if len(message.text[5:len(message.text)]) <= 9:
            bot.send_message(message.chat.id, eval(message.text[5:len(message.text)]))
            uses.append((message.chat.id, 'calculate', str(datetime.now())[:19]))
            print(f'{message.chat.id} used calculator to solve {message.text[5:len(message.text)]}')
    elif message.text.lower() == 'wfa':
        playsound('bells.mp3')
        bot.send_message(message.chat.id, input("The user wants your word: "))
        uses.append((message.chat.id, 'wanted word', str(datetime.now())[:19]))
    # elif message.chat.id == 1600275920:
    #    while True:
    #        bot.send_message(message.chat.id, "SPAM!!!")
    else:
        bot.send_message(
            message.chat.id,
            'Не не, ты меня не проведёшь! Введи цифру от 1 до 19: ')
    print(uses)

@bot.message_handler(commands=['go'])
def hello2(message):
    bot.send_message(
        message.chat.id,
        'Привет, напиши мне любую цифру от 10 до 19, а я тебе пришлю анекдот: ')


bot.polling()
