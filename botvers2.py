import telebot
from telebot import types
import random
import time

token = '2121107187:AAF-7ZORYiFHZATunaPEzw5c4IrP-AuGR0Q'
bot = telebot.TeleBot(token=token)

biz = 0
pres = 0
jud = 0
noha = 0
vitrumka = 5
languag = 'ukr'


@bot.message_handler(commands=['start'])
def start(messege):
    bot.send_message(messege.chat.id,
                     text='привіт!\n це симулятор спортсмена)\n якщо хочеш грати натисни: /sport\nякщо хочеш змінити мову: /language')


@bot.message_handler(commands=['sport'])
def f(messege):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='💪качатись💪')
    button2 = types.KeyboardButton(text='📊статистика📊')
    button3 = types.KeyboardButton(text='💸донат💸')
    button4 = types.KeyboardButton(text='магазин')
    button5 = types.KeyboardButton(text='ти адмін....')
    button1eng = types.KeyboardButton(text='💪training💪')
    button2eng = types.KeyboardButton(text='📊statistics📊')
    button3eng = types.KeyboardButton(text='💸donate💸')
    button4eng = types.KeyboardButton(text='shop')
    if languag == 'ukr':
        if messege.chat.first_name != 'Вітер🌪':
            button.add(button1, button2, button3, )
            messege_from_user = bot.send_message(messege.chat.id, text='вітаю в меню🍾',
                                                 reply_markup=button)
            bot.register_next_step_handler(messege_from_user,
                                           dija)
        else:
            button.add(button1, button2, button3, button5)
            messege_from_user = bot.send_message(messege.chat.id, text='ти в меню',
                                                 reply_markup=button)
            bot.register_next_step_handler(messege_from_user,
                                           dija)
    elif languag == 'eng':
        button.add(button1eng, button2eng, button3eng, )
        messege_from_user = bot.send_message(messege.chat.id, text='hello!! i am glad to see you🍾',
                                             reply_markup=button)
        bot.register_next_step_handler(messege_from_user,
                                   dija)


@bot.message_handler(commands=['language'])
def language(messege):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Україньська')
    button2 = types.KeyboardButton(text='English')
    button.add(button1, button2)
    messege_from_user = bot.send_message(messege.chat.id, text='вибери свою мову',
                                         reply_markup=button)
    bot.register_next_step_handler(messege_from_user,
                                   mova)


def mova(messege):
    global languag
    if messege.text == 'Україньська':
        languag = 'ukr'
        f(messege)
    elif messege.text == 'English':
        languag = 'eng'
        f(messege)


def dija(messege):
    print(messege.chat.first_name)
    if messege.text == '💪качатись💪':
        klick(messege)
    elif messege.text == '💪training💪':
        klick(messege)
    elif messege.text == '📊статистика📊':
        info(messege)
    elif messege.text == '📊statistics📊':
        info(messege)
    elif messege.text == '💸донат💸':
        donat(messege)
    elif messege.text == '💸donate💸':
        donat(messege)
    elif messege.text == 'магазин':
        f(messege)
    elif messege.text == 'shop':
        f(messege)
    elif messege.text == 'ти адмін....':
        admin(messege)


def admin(messege):
    pass


def donat(messege):
    global languag
    button = types.ReplyKeyboardRemove(selective=False)
    if languag == 'ukr':
        карта = bot.send_message(messege.chat.id,
                                 text='''накинь пару гривень 4441114431333275 і автор надішле код🫥 \n❗якщо хочеш повернутись напиши; 'назад в меню'❗ ''',
                                 reply_markup=button)
    if languag == 'eng':
        карта = bot.send_message(messege.chat.id,
                                 text='''throw in a couple of hryvnias 4441114431333275 and the author will send the code🫥\n❗ if you want to return, write; 'back to menu'❗ ''',
                                 reply_markup=button)

    bot.register_next_step_handler(карта,
                                   ggg)


def ggg(messege):
    global languag
    if messege.text == 'назад в меню':
        f(messege)
    elif messege.text == 'back to menu':
        f(messege)
    elif messege.text == 'теплийтоп':
        bot.send_message(messege.chat.id, text=f'плюс 10 см до твоїх мязів')
        f(messege)
    else:
        if languag == 'ukr':
            bot.send_message(messege.chat.id, text='❌КОД НЕ ВІРНИЙ❌')
            f(messege)
        elif languag == 'eng':
            bot.send_message(messege.chat.id, text='❌THE CODE IS NOT VALID❌')
            f(messege)


def klick(messege):
    global languag
    global biz, noha, jud, pres
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='💪качати біцепс💪')
    button3 = types.KeyboardButton(text='🔥качати спину🔥')
    button4 = types.KeyboardButton(text='🏆качати прес🏆')
    button5 = types.KeyboardButton(text='📄назад в меню📄')
    button1eng = types.KeyboardButton(text='💪pump biceps💪')
    button3eng = types.KeyboardButton(text='🔥rock your back🔥')
    button4eng = types.KeyboardButton(text='🏆pump abs🏆')
    button5eng = types.KeyboardButton(text='📄back to menu📄')
    if languag == 'ukr':
        button.add(button1, button3, button4, button5)
        messege_from_user = bot.send_message(messege.chat.id, text=f'надіюсь ти зможеш віджатись ще хоч раз...',
                                             reply_markup=button)
        bot.register_next_step_handler(messege_from_user,
                                       klik2)
    elif languag == 'eng':
        button.add(button1eng, button3eng, button4eng, button5eng)
        messege_from_user = bot.send_message(messege.chat.id, text=f'Hope you can push up in one more time...',
                                             reply_markup=button)
        bot.register_next_step_handler(messege_from_user,
                                   klik2)


def klik2(messege):
    global languag
    global biz, noha, jud, pres
    n = random.randint(1, 10)
    print(n)
    if languag == 'ukr':
        if n != 3 :

            if messege.text == '💪качати біцепс💪':
                if n == 5:
                    bot.send_message(messege.chat.id,
                                     text=f'пульс 150🫀...\nце могло бути твоє останє віджимання)')
                    bot.send_message(messege.chat.id, text=f'🫀')
                    klick(messege)
                else:
                    bot.send_message(messege.chat.id,
                                     text=f'вітаю🍾🍾\nти зміг віджатись 1 раз')
                    biz = biz + 0.1
                    klick(messege)


            elif messege.text == '🔥качати спину🔥':
                if n == 5:
                    bot.send_message(messege.chat.id,
                                     text=f'пульс 150🫀...\nце могло бути твоє останє підтягування)')
                    bot.send_message(messege.chat.id, text=f'🫀')
                    klick(messege)
                else:
                    bot.send_message(messege.chat.id,
                                     text=f'вітаю🍾🍾\nти зміг підтянутись 1 раз')
                    jud = jud + 1
                    klick(messege)


            elif messege.text == '🏆качати прес🏆':
                if n == 5:
                    bot.send_message(messege.chat.id,
                                     text=f'пульс 150🫀...\nце могло бути твоє останє заняття)')
                    bot.send_message(messege.chat.id, text=f'🫀')
                    klick(messege)
                else:
                    bot.send_message(messege.chat.id,
                                     text=f'вітаю🍾🍾\nти "зробив велосипед" 1 раз')
                    pres = pres + 0.1
                    klick(messege)
            elif messege.text == '📄назад в меню📄':
                f(messege)
        elif n == 3:
            if messege.text == '📄назад в меню📄':
                f(messege)
            else:
                bot.send_message(messege.chat.id, text=f'ти перенапружився і впав в обмарок💀...\nрозмір усіх мязів -0.5 мм\nтепер мусиш відпочити 10 сек')
                bot.send_message(messege.chat.id, text=f'💀')
                time.sleep(10)
                biz = biz - 0.5
                jud = jud - 5
                pres = pres - 0.5
                klick(messege)
    elif languag == 'eng':
        if n != 3 :

            if messege.text == '💪pump biceps💪':
                if n == 5:
                    bot.send_message(messege.chat.id,
                                     text=f'heart rate 150🫀...\n this could be your last push up)')
                    bot.send_message(messege.chat.id, text=f'🫀')
                    klick(messege)
                else:
                    bot.send_message(messege.chat.id,
                                     text=f'congratulations🍾🍾\nyou were able to push up 1 time')
                    biz = biz + 0.1
                    klick(messege)


            elif messege.text == '🔥rock your back🔥':
                if n == 5:
                    bot.send_message(messege.chat.id,
                                     text=f'heart rate 150🫀...\n this could be your last pull-up)')
                    bot.send_message(messege.chat.id, text=f'🫀')
                    klick(messege)
                else:
                    bot.send_message(messege.chat.id,
                                     text=f'congratulations🍾🍾\nyou were able to pull up 1 time')
                    jud = jud + 1
                    klick(messege)


            elif messege.text == '🏆pump abs🏆':
                if n == 5:
                    bot.send_message(messege.chat.id,
                                     text=f'heart rate 150🫀...\n this could be your last training)')
                    bot.send_message(messege.chat.id, text=f'🫀')
                    klick(messege)
                else:
                    bot.send_message(messege.chat.id,
                                     text=f'congratulations🍾🍾\nyou have "made a bike" 1 time')
                    pres = pres + 0.1
                    klick(messege)
            elif messege.text == '📄back to menu📄':
                f(messege)
        elif n == 3:
            if messege.text == '📄back to menu📄':
                f(messege)
            else:
                bot.send_message(messege.chat.id, text=f'you overexerted yourself and fainted💀...\nsize of all muscles -0.5 mm\nnow you have to rest for 10 seconds')
                bot.send_message(messege.chat.id, text=f'💀')
                time.sleep(10)
                biz = biz - 0.5
                jud = jud - 5
                pres = pres - 0.5
                klick(messege)



def info(messege):
    global languag
    global biz, noha, jud, pres
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='📄назад в меню📄')
    button1eng = types.KeyboardButton(text='📄back to menu📄')
    if languag == 'ukr':
        button.add(button1)
        h = bot.send_message(messege.chat.id,
                             text=f'нічого собі... та ти як шварцнегр🥇)\n - твій біцепс: {biz} мм💪\n - твоя спина: {jud} / 999🔥\n - твій прес: {pres} мм🏆', reply_markup=button)
        bot.register_next_step_handler(h,
                                   klik2)
    elif languag == 'eng':
        button.add(button1eng)
        h = bot.send_message(messege.chat.id,
                             text=f'nothing... and youre like a Schwarzenegger🥇)\n - your biceps: {biz} mm💪\n - your back: {jud} / 999🔥\n - your abs: {pres} mm🏆',
                             reply_markup=button)
        bot.register_next_step_handler(h,
                                       klik2)


if __name__ == '__main__':
    bot.polling(non_stop=True)
