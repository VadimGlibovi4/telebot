#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
from telebot import types
import telebot
import db
import config
import importlib
import sys
importlib.reload(sys)


token = config.token
bot = telebot.TeleBot(token)


# keyboard
# welcome_keyboard
sold_button = types.KeyboardButton('Я продал шеврон')
correct_button = types.KeyboardButton('Скоректировать продажу')
add_new_button = types.KeyboardButton('Поступили шевроны')
residue_button = types.KeyboardButton('Остаток шевронов')
main_report_button = types.KeyboardButton('Рассчитать')
all_sold_button = types.KeyboardButton('Всего продано')
actual_price = types.KeyboardButton('Цены')
price_button = types.KeyboardButton('Изменить цены')
kek_button = types.KeyboardButton("Юху я долбаеб нахуй😜")
reboot_button = types.KeyboardButton("/start")

# sold_keyboard
mw_butt = types.InlineKeyboardButton("MW", callback_data="MW")
mw_veteran_butt = types.InlineKeyboardButton("MW_Ветеран", callback_data="MW_Veteran")
mw_complect_butt = types.InlineKeyboardButton("Комплект_Воина", callback_data="Complect_Voina")

arab_butt = types.InlineKeyboardButton("Арабский", callback_data="Arab")
russ_butt = types.InlineKeyboardButton("Русский", callback_data="Russ")

quarantine_butt = types.InlineKeyboardButton("Quarantine", callback_data="Quarantine")
covid_veter_butt = types.InlineKeyboardButton("COVID_Ветеран", callback_data="COVID_Veteran")
quarantine_complect_butt = types.InlineKeyboardButton("Комплект_Карантин",
                                                      callback_data="Complect_Quarantine")

sold_keyboard_buttons = [mw_butt, mw_veteran_butt, mw_complect_butt, arab_butt,
                         russ_butt, quarantine_butt, covid_veter_butt, quarantine_complect_butt]


# add_new_keyboard
mw_butt_new = types.InlineKeyboardButton("MW", callback_data="MW_new")
mw_veteran_butt_new = types.InlineKeyboardButton("MW_Ветеран", callback_data="MW_Veteran_new")


arab_butt_new = types.InlineKeyboardButton("Арабский", callback_data="Arab_new")
russ_butt_new = types.InlineKeyboardButton("Русский", callback_data="Russ_new")

quarantine_butt_new = types.InlineKeyboardButton("Quarantine", callback_data="Quarantine_new")
covid_veter_butt_new = types.InlineKeyboardButton("COVID_Ветеран", callback_data="COVID_Veteran_new")


add_new_keyboard_buttons = [mw_butt_new, mw_veteran_butt_new, arab_butt_new,
                            russ_butt_new, quarantine_butt_new, covid_veter_butt_new]

# new price keyboard
mw_butt_price = types.InlineKeyboardButton("MW", callback_data="MW_price")
mw_veteran_butt_price = types.InlineKeyboardButton("MW_Ветеран", callback_data="MW_Veteran_price")
mw_complect_butt_price = types.InlineKeyboardButton("Комплект_Воина", callback_data="Complect_Voina_price")

arab_butt_price = types.InlineKeyboardButton("Арабский", callback_data="Arab_price")
russ_butt_price = types.InlineKeyboardButton("Русский", callback_data="Russ_price")

quarantine_butt_price = types.InlineKeyboardButton("Quarantine", callback_data="Quarantine_price")
covid_veter_butt_price = types.InlineKeyboardButton("COVID_Ветеран", callback_data="COVID_Veteran_price")
quarantine_complect_butt_price = types.InlineKeyboardButton("Комплект_Карантин",
                                                            callback_data="Complect_Quarantine_price")

new_price_keyboard_buttons = [mw_butt_price, mw_veteran_butt_price, mw_complect_butt_price, arab_butt_price,
                              russ_butt_price, quarantine_butt_price, covid_veter_butt_price,
                              quarantine_complect_butt_price]

# correct_sold_keyboard
mw_butt_correct = types.InlineKeyboardButton("MW", callback_data="MW_correct")
mw_veteran_butt_correct = types.InlineKeyboardButton("MW_Ветеран", callback_data="MW_Veteran_correct")
mw_complect_butt_correct = types.InlineKeyboardButton("Комплект_Воина", callback_data="Complect_Voina_correct")

arab_butt_correct = types.InlineKeyboardButton("Арабский", callback_data="Arab_correct")
russ_butt_correct = types.InlineKeyboardButton("Русский", callback_data="Russ_correct")

quarantine_butt_correct = types.InlineKeyboardButton("Quarantine", callback_data="Quarantine_correct")
covid_veter_butt_correct = types.InlineKeyboardButton("COVID_Ветеран", callback_data="COVID_Veter_correct")
quarantine_complect_butt_correct = types.InlineKeyboardButton("Комплект_Карантин",
                                                              callback_data="Complect_Quarantine_correct")


yes_button = types.InlineKeyboardButton('Продолжить..', callback_data='Continue')


@bot.message_handler(commands=['start'])
def welcome(message):
    markup_full = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_anon = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup_full.add(sold_button, correct_button,add_new_button, residue_button, main_report_button, all_sold_button,
                    actual_price, price_button, kek_button, reboot_button)
    markup_anon.add(kek_button)

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    anonymous = message.from_user.username
    chat_id = message.chat.id
    print('------')
    try:
        print('User with name {} {} and nickname {} '
              'and chat_id = {} is connected'.format(first_name, last_name, anonymous, chat_id))
    except Exception as e:
        print(f'User with unknown name and {anonymous} nickname is connected!')
    print('------')

    if anonymous == config.users_names[0]:
        if chat_id != config.chat_id_list[0]:
            print('Attention! Chat_id {} for user {} '
                  'is different from db {}'.format(chat_id, config.users_names[0], config.chat_id_list[0]))
            db.update_chat_id(user_name=config.users_names[0],
                              chat_id=chat_id)
            config.chat_id_list.pop(0)
            config.chat_id_list.insert(0, chat_id)

    if anonymous == config.users_names[1]:
        if chat_id != config.chat_id_list[1]:
            print('Attention! Chat_id {} for user {} '
                  'is different from db {}'.format(chat_id, config.users_names[1], config.chat_id_list[1]))
            db.update_chat_id(user_name=config.users_names[1],
                              chat_id=chat_id)
            config.chat_id_list.pop(1)
            config.chat_id_list.insert(1, chat_id)

    welcome_message_text = '{} {}, МОИ ДОГ! КАК ДЕЛА? 3И, ДЕТКА, ТЫ В ПОРЯДКЕ, ЧУВАК?'.format(first_name, last_name)
    if anonymous in config.users_names:
        bot.send_message(message.chat.id, welcome_message_text, reply_markup=markup_full)
    else:
        bot.send_photo(message.chat.id, open('forbidden.jpg', 'rb'))
        bot.send_message(message.chat.id, "Вы кто такие?! Я вас не звал! Идите на*хуй!", reply_markup=markup_anon)

# главная клавиатура


@bot.message_handler(content_types=["text"])
def keyboard(message):
    if message.chat.type == 'private':
        anonymous = message.from_user.username
        if anonymous in config.users_names:
            if message.text == sold_button.text:
                if message.from_user.username == config.users_names[0]:
                    sold_keyboard = types.InlineKeyboardMarkup(row_width=2)
                    sold_keyboard.add(mw_butt, mw_veteran_butt, mw_complect_butt, arab_butt, russ_butt,
                                      quarantine_butt, covid_veter_butt, quarantine_complect_butt)

                    bot.send_message(message.chat.id, 'Выбери какой шеврон ты продал:', reply_markup=sold_keyboard)
                else:
                    bot.send_message(message.chat.id, 'Ты за меня придурка не держи, ладно?')

            if message.text == correct_button.text:
                if message.from_user.username == config.users_names[0]:
                    correct_keyboard = types.InlineKeyboardMarkup(row_width=2)
                    correct_keyboard.add(mw_butt_correct, mw_veteran_butt_correct, mw_complect_butt_correct,
                                         arab_butt_correct, russ_butt_correct, quarantine_butt_correct,
                                         covid_veter_butt_correct, quarantine_complect_butt_correct)

                    bot.send_message(message.chat.id, 'Какой откорректировать:', reply_markup=correct_keyboard)
                else:
                    bot.send_message(message.chat.id, 'Ты за меня придурка не держи, ладно?')

            if message.text == add_new_button.text:
                if message.from_user.username == config.users_names[0]:

                    add_new_keyboard = types.InlineKeyboardMarkup(row_width=2)
                    add_new_keyboard.add(mw_butt_new, mw_veteran_butt_new, arab_butt_new,
                                         russ_butt_new, quarantine_butt_new, covid_veter_butt_new
                                         )

                    bot.send_message(message.chat.id, "Какой:", reply_markup=add_new_keyboard)

                else:
                    bot.send_message(message.chat.id, 'Ты за меня придурка не держи, ладно?')

            if message.text == residue_button.text:
                bot.send_message(message.chat.id, "Считаю...")
                residue = db.select_from_all_chevrons()

                residue_message = '\n'.join(f'{k[0]}: {k[1]}шт.' for k in residue.items())

                bot.send_message(message.chat.id, residue_message)

            if message.text == main_report_button.text:
                continue_keyboard = types.InlineKeyboardMarkup(row_width=1)
                continue_keyboard.add(yes_button)

                bot.send_message(message.chat.id, 'Отчёт сделает сброс в таблице проданных шевронов!',
                                 reply_markup=continue_keyboard)

            if message.text == all_sold_button.text:
                all_sold_value = db.select_from_sold_chevrons()
                bot.send_message(message.chat.id, f'Продано всего:\n'
                                                  f'{mw_butt.text}: {all_sold_value[mw_butt.callback_data]}\n'
                                                  f'{mw_veteran_butt.text}: {all_sold_value[mw_veteran_butt.callback_data]}\n'
                                                  f'{mw_complect_butt.text}: {all_sold_value[mw_complect_butt.callback_data]}\n'
                                                  f'{arab_butt.text}:  {all_sold_value[arab_butt.callback_data]}\n'
                                                  f'{russ_butt.text}: {all_sold_value[russ_butt.callback_data]}\n'
                                                  f'{quarantine_butt.text}: {all_sold_value[quarantine_butt.callback_data]}\n'
                                                  f'{covid_veter_butt.text}: {all_sold_value[covid_veter_butt.callback_data]}\n'
                                                  f'{quarantine_complect_butt.text}: '
                                                  f'{all_sold_value[quarantine_complect_butt.callback_data]}')

            if message.text == actual_price.text:
                price = db.get_price()
                bot.send_message(message.chat.id, 'Цена на шевроны:\n'
                                                  f'{mw_butt.text}: {price[mw_butt.callback_data]}\n'
                                                  f'{mw_veteran_butt.text}: {price[mw_veteran_butt.callback_data]}\n'
                                                  f'{mw_complect_butt.text}: {price[mw_complect_butt.callback_data]}\n'
                                                  f'{arab_butt.text}:  {price[arab_butt.callback_data]}\n'
                                                  f'{russ_butt.text}: {price[russ_butt.callback_data]}\n'
                                                  f'{quarantine_butt.text}: {price[quarantine_butt.callback_data]}\n'
                                                  f'{covid_veter_butt.text}: {price[covid_veter_butt.callback_data]}\n'
                                                  f'{quarantine_complect_butt.text}: '
                                                  f'{price[quarantine_complect_butt.callback_data]}')

            if message.text == price_button.text:
                new_price_keyboard = types.InlineKeyboardMarkup(row_width=2)
                new_price_keyboard.add(mw_butt_price, mw_veteran_butt_price, mw_complect_butt_price, arab_butt_price,
                                       russ_butt_price, quarantine_butt_price, covid_veter_butt_price,
                                       quarantine_complect_butt_price)

                price = db.get_price()
                bot.send_message(message.chat.id, 'Цена на шевроны:\n'
                                                  f'{mw_butt.text}: {price[mw_butt.callback_data]}\n'
                                                  f'{mw_veteran_butt.text}: {price[mw_veteran_butt.callback_data]}\n'
                                                  f'{mw_complect_butt.text}: {price[mw_complect_butt.callback_data]}\n'
                                                  f'{arab_butt.text}:  {price[arab_butt.callback_data]}\n'
                                                  f'{russ_butt.text}: {price[russ_butt.callback_data]}\n'
                                                  f'{quarantine_butt.text}: {price[quarantine_butt.callback_data]}\n'
                                                  f'{covid_veter_butt.text}: {price[covid_veter_butt.callback_data]}\n'
                                                  f'{quarantine_complect_butt.text}: '
                                                  f'{price[quarantine_complect_butt.callback_data]}')
                bot.send_message(message.chat.id, 'На какой шеврон изменить цену?', reply_markup=new_price_keyboard)

        if message.text == kek_button.text:
            print(f'{anonymous} click on kek_button')
            gif = open("coffin.gif", 'rb')
            bot.send_animation(message.chat.id, gif)
            bot.send_message(message.chat.id, 'Ебать братишка ты долбаёб, земля тебе пухом)0')

        if anonymous not in config.users_names:
            bot.send_photo(message.chat.id, open('forbidden.jpg', 'rb'))
            bot.send_message(message.chat.id, "Вы кто такие?! Я вас не звал! Идите на*хуй!")

# продан шеврон, функционал клавиатуры


sold_info_message = "Красава, так и запишу, {} +1 проданный шеврон"
sold_all_info_message = 'Всего продано {} {}. Остаток: {}'

sold_complect_message = "Красава, так и запишу, {} +1 проданный комплект"
sold_complect_info_message = 'Всего продано \n{}: {}.\nОстаток по шевронам:\n{}: {},\n{}: {}'

add_new_info_message = "Сейчас в наличии {} {}. Сколько добавить?"

correct_info_message = "Ладно, так и запишу, {} -1 проданный шеврон"
correct_all_info_message = 'Продано теперь {} Остаток: {}'


correct_complect_message = "Ладно, так и запишу, {} -1 проданный комплект"
correct_complect_info_message = 'Всего продано теперь \n{}: {}.\nОстаток по шевронам:\n{}: {},\n{}: {}'

which_button = ''
new_price_message = 'Какую сделать цену на {}?'


@bot.callback_query_handler(func=lambda call: True)
def sold(call):
    try:
        if call.message:
            name_user = call.from_user.first_name
            last_name = call.from_user.last_name
            print(f'{name_user} {last_name} press {call.data} button')
            global which_button
            if call.data == mw_butt.callback_data:
                which_button = mw_butt.callback_data
                bot.send_message(call.message.chat.id, sold_info_message.format(mw_butt.text))
                all_sold = db.add_sold_value(chevron_name=mw_butt.callback_data)

            if call.data == mw_veteran_butt.callback_data:
                which_button = mw_veteran_butt.callback_data
                bot.send_message(call.message.chat.id, sold_info_message.format(mw_veteran_butt.text))
                all_sold = db.add_sold_value(chevron_name=mw_veteran_butt.callback_data)

            if call.data == mw_complect_butt.callback_data:
                which_button = mw_complect_butt.callback_data
                bot.send_message(call.message.chat.id, sold_complect_message.format(mw_complect_butt.text))
                all_sold_complect = db.add_sold_complect_value(complect_name=mw_complect_butt.callback_data)

                bot.send_message(call.message.chat.id,
                                 sold_complect_info_message.format(mw_complect_butt.text,
                                                                   all_sold_complect[mw_complect_butt.callback_data],
                                                                   mw_butt.text,
                                                                   all_sold_complect[mw_butt.callback_data],
                                                                   mw_veteran_butt.text,
                                                                   all_sold_complect[mw_veteran_butt.callback_data]
                                                                   )
                                 )

                if all_sold_complect[mw_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {mw_butt.text} осталось всего {all_sold_complect[mw_butt.callback_data]} !')

                if all_sold_complect[mw_veteran_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {mw_veteran_butt.text} осталось всего '
                                                  f'{all_sold_complect[mw_veteran_butt.callback_data]} !')

            if call.data == arab_butt.callback_data:
                which_button = arab_butt.callback_data
                bot.send_message(call.message.chat.id, sold_info_message.format(arab_butt.text))
                all_sold = db.add_sold_value(chevron_name=arab_butt.callback_data)

            if call.data == russ_butt.callback_data:
                which_button = russ_butt.callback_data
                bot.send_message(call.message.chat.id, sold_info_message.format(russ_butt.text))
                all_sold = db.add_sold_value(chevron_name=russ_butt.callback_data)

            if call.data == quarantine_butt.callback_data:
                which_button = quarantine_butt.callback_data
                bot.send_message(call.message.chat.id, sold_info_message.format(quarantine_butt.text))
                all_sold = db.add_sold_value(chevron_name=quarantine_butt.callback_data)

            if call.data == covid_veter_butt.callback_data:
                which_button = covid_veter_butt.callback_data
                bot.send_message(call.message.chat.id, sold_info_message.format(covid_veter_butt.text))
                all_sold = db.add_sold_value(chevron_name=covid_veter_butt.callback_data)

            if call.data == quarantine_complect_butt.callback_data:
                which_button = quarantine_complect_butt.callback_data
                all_sold_complect = db.add_sold_complect_value(complect_name=quarantine_complect_butt.callback_data)
                bot.send_message(call.message.chat.id, sold_complect_message.format(quarantine_complect_butt.text))

                bot.send_message(call.message.chat.id,
                                 sold_complect_info_message.format(quarantine_complect_butt.text,
                                                                   all_sold_complect[quarantine_complect_butt.callback_data],
                                                                   quarantine_butt.text,
                                                                   all_sold_complect[quarantine_butt.callback_data],
                                                                   covid_veter_butt.text,
                                                                   all_sold_complect[covid_veter_butt.callback_data]
                                                                   )
                                 )

                if all_sold_complect[quarantine_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {quarantine_butt.text} осталось всего'
                                                  f' {all_sold_complect[quarantine_butt.callback_data]} !')

                if all_sold_complect[covid_veter_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {covid_veter_butt.text} осталось всего '
                                                  f'{all_sold_complect[covid_veter_butt.callback_data]} !')
            # new_chevron_keyboard

            if call.data == mw_butt_new.callback_data:
                which_button = mw_butt.callback_data
                count = db.select_from_all_chevrons(mw_butt.callback_data)[0]
                msg = bot.send_message(call.message.chat.id,
                                       add_new_info_message.format(count, mw_butt_new.text))

                bot.register_next_step_handler(msg, add_new_chevrons)

            if call.data == mw_veteran_butt_new.callback_data:
                which_button = mw_veteran_butt.callback_data
                count = db.select_from_all_chevrons(mw_veteran_butt.callback_data)[0]
                msg = bot.send_message(call.message.chat.id,
                                       add_new_info_message.format(count, mw_veteran_butt_new.text))

                bot.register_next_step_handler(msg, add_new_chevrons)

            if call.data == arab_butt_new.callback_data:
                which_button = arab_butt.callback_data
                count = db.select_from_all_chevrons(arab_butt.callback_data)[0]
                msg = bot.send_message(call.message.chat.id,
                                       add_new_info_message.format(count, arab_butt_new.text))

                bot.register_next_step_handler(msg, add_new_chevrons)

            if call.data == russ_butt_new.callback_data:
                which_button = russ_butt.callback_data
                count = db.select_from_all_chevrons(russ_butt.callback_data)[0]
                msg = bot.send_message(call.message.chat.id,
                                       add_new_info_message.format(count, russ_butt_new.text))

                bot.register_next_step_handler(msg, add_new_chevrons)

            if call.data == covid_veter_butt_new.callback_data:
                which_button = covid_veter_butt.callback_data
                count = db.select_from_all_chevrons(covid_veter_butt.callback_data)[0]
                msg = bot.send_message(call.message.chat.id,
                                       add_new_info_message.format(count, covid_veter_butt_new.text))

                bot.register_next_step_handler(msg, add_new_chevrons)

            if call.data == quarantine_butt_new.callback_data:
                which_button = quarantine_butt.callback_data
                count = db.select_from_all_chevrons(quarantine_butt.callback_data)[0]
                msg = bot.send_message(call.message.chat.id,
                                       add_new_info_message.format(count, quarantine_butt_new.text))

                bot.register_next_step_handler(msg, add_new_chevrons)

            # new price keyboard

            if call.data == mw_butt_price.callback_data:
                which_button = mw_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(mw_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == mw_veteran_butt_price.callback_data:
                which_button = mw_veteran_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(mw_veteran_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == mw_complect_butt_price.callback_data:
                which_button = mw_complect_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(mw_complect_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == arab_butt_price.callback_data:
                which_button = arab_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(arab_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == russ_butt_price.callback_data:
                which_button = russ_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(russ_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == covid_veter_butt_price.callback_data:
                which_button = covid_veter_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(covid_veter_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == quarantine_butt_price.callback_data:
                which_button = quarantine_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(quarantine_butt.text))
                bot.register_next_step_handler(msg, update_price)

            if call.data == quarantine_complect_butt_price.callback_data:
                which_button = quarantine_complect_butt.callback_data
                msg = bot.send_message(call.message.chat.id, new_price_message.format(quarantine_complect_butt.text))
                bot.register_next_step_handler(msg, update_price)

            # correct_keyboard

            if call.data == mw_butt_correct.callback_data:
                bot.send_message(call.message.chat.id, correct_info_message.format(mw_butt_correct.text))
                all_sold = db.correct_sold_value(chevron_name=mw_butt.callback_data)
                bot.send_message(call.message.chat.id, correct_all_info_message.format(all_sold['Sold_All'],
                                                                                       all_sold['All']))

            if call.data == mw_veteran_butt_correct.callback_data:
                bot.send_message(call.message.chat.id, correct_info_message.format(mw_veteran_butt_correct.text))
                all_sold = db.correct_sold_value(chevron_name=mw_veteran_butt.callback_data)
                bot.send_message(call.message.chat.id, correct_all_info_message.format(all_sold['Sold_All'],
                                                                                       all_sold['All']))

            if call.data == mw_complect_butt_correct.callback_data:
                bot.send_message(call.message.chat.id,
                                 correct_info_message.format(mw_complect_butt_correct.text))
                correct = db.correct_sold_complect_value(complect_name=mw_complect_butt.callback_data)
                print(correct)

                bot.send_message(call.message.chat.id,
                                 correct_complect_info_message.format(mw_complect_butt.text,
                                                                 correct[mw_complect_butt.callback_data],
                                                                 mw_butt.text,
                                                                 correct[mw_butt.callback_data],
                                                                 mw_veteran_butt.text,
                                                                 correct[mw_veteran_butt.callback_data]
                                                                )
                                 )
                if correct[mw_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {mw_butt.text} осталось всего {correct[mw_butt.callback_data]} !')

                if correct[mw_veteran_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {mw_veteran_butt.text} осталось всего '
                                                  f'{correct[mw_veteran_butt.callback_data]} !')

            if call.data == arab_butt_correct.callback_data:
                bot.send_message(call.message.chat.id, correct_info_message.format(arab_butt_correct.text))
                all_sold = db.correct_sold_value(chevron_name=arab_butt.callback_data)
                bot.send_message(call.message.chat.id, correct_all_info_message.format(all_sold['Sold_All'],
                                                                                       all_sold['All']))

            if call.data == russ_butt_correct.callback_data:
                bot.send_message(call.message.chat.id, correct_info_message.format(russ_butt_correct.text))
                all_sold = db.correct_sold_value(chevron_name=russ_butt.callback_data)
                bot.send_message(call.message.chat.id, correct_all_info_message.format(all_sold['Sold_All'],
                                                                                       all_sold['All']))

            if call.data == quarantine_butt_correct.callback_data:
                bot.send_message(call.message.chat.id, correct_info_message.format(quarantine_butt_correct.text))
                all_sold = db.correct_sold_value(chevron_name=quarantine_butt.callback_data)
                bot.send_message(call.message.chat.id, correct_all_info_message.format(all_sold['Sold_All'],
                                                                                       all_sold['All']))

            if call.data == covid_veter_butt_correct.callback_data:
                bot.send_message(call.message.chat.id, correct_info_message.format(covid_veter_butt_correct.text))
                all_sold = db.correct_sold_value(chevron_name=covid_veter_butt.callback_data)
                bot.send_message(call.message.chat.id, correct_all_info_message.format(all_sold['Sold_All'],
                                                                                       all_sold['All']))

            if call.data == quarantine_complect_butt_correct.callback_data:
                bot.send_message(call.message.chat.id,
                                 correct_info_message.format(quarantine_complect_butt_correct.text))
                correct = db.correct_sold_complect_value(complect_name=quarantine_complect_butt.callback_data)

                bot.send_message(call.message.chat.id,
                                 correct_complect_info_message.format(quarantine_complect_butt.text,
                                                                      correct[quarantine_complect_butt.callback_data],
                                                                      quarantine_butt.text,
                                                                      correct[quarantine_butt.callback_data],
                                                                      covid_veter_butt.text,
                                                                      correct[covid_veter_butt.callback_data]
                                                                      )
                                 )
                if correct[quarantine_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {quarantine_butt.text} осталось '
                                                  f'всего {correct[quarantine_butt.callback_data]} !')

                if correct[covid_veter_butt.callback_data] < 3:
                    for chat_id in config.chat_id_list:
                        bot.send_message(chat_id, f'Shit! {covid_veter_butt.text} осталось всего '
                                                  f'{correct[covid_veter_butt.callback_data]} !')


            # report

            if call.data == yes_button.callback_data:
                all_chevrons = db.main_report()
                all_sold_report = db.select_from_sold_chevrons()

                report_message = 'Итак, дружок, полный отчёт по шевронам таков:\n' \
                f'{mw_butt.text}: {all_sold_report[mw_butt.callback_data]} шт на {all_chevrons[0][mw_butt.callback_data]} рубасей.\n' \
                f'{mw_veteran_butt.text}: {all_sold_report[mw_veteran_butt.callback_data]} шт ' \
                f'на {all_chevrons[0][mw_veteran_butt.callback_data]} рубасей.\n' \
                f'{mw_complect_butt.text}: {all_sold_report[mw_complect_butt.callback_data]} шт ' \
                f'на {all_chevrons[0][mw_complect_butt.callback_data]} рубасей.\n' \
                f'{arab_butt.text}: {all_sold_report[arab_butt.callback_data]} шт' \
                f' на {all_chevrons[0][arab_butt.callback_data]} рубасей.\n' \
                f'{russ_butt.text}: {all_sold_report[russ_butt.callback_data]} шт ' \
                f'на {all_chevrons[0][russ_butt.callback_data]} рубасей.\n' \
                f'{quarantine_butt.text}: {all_sold_report[quarantine_butt.callback_data]} шт ' \
                f'на {all_chevrons[0][quarantine_butt.callback_data]} рубасей.\n' \
                f'{covid_veter_butt.text}: {all_sold_report[covid_veter_butt.callback_data]} шт ' \
                f'на {all_chevrons[0][covid_veter_butt.callback_data]} рубасей.\n' \
                f'{quarantine_complect_butt.text}: {all_sold_report[quarantine_complect_butt.callback_data]} шт' \
                f' на {all_chevrons[0][quarantine_complect_butt.callback_data]} рубасей.\n'

                print('calculate report')
                actual_exchange = db.get_actual_exchange()
                all_rub = all_chevrons[1]['All_money_rub']
                all_hrn = all_rub * actual_exchange[0]
                one_person_rub = (all_chevrons[1]['All_money_rub'] / 2)
                one_person_uah = one_person_rub * actual_exchange[0]

                for chat_id in config.chat_id_list:
                    print(f'Send report to {chat_id} user')

                    bot.send_message(chat_id, report_message)

                    bot.send_message(chat_id,
                                     f"Сумма за все {all_chevrons[2]['All_count']} шт "
                                     f" = {all_rub} руб или {all_hrn}грн\n"
                                     f"Итого кажому {one_person_rub} руб или {one_person_uah} грн.\n"
                                     f"Курс рубля: {actual_exchange[0]}\n"
                                     f"Как всегда, спасибо за внимание!")

                    if one_person_uah < 300:
                        bot.send_message(chat_id, 'Ну, тут конечно даже не попьёшь шампансккое кристал.')
                    else:
                        bot.send_message(chat_id, f'Открывай шампанское кристал, комрад!')

                db.set_0_value_in_sold_table()

        if all_sold['All'] < 2:
            for chat_id in config.chat_id_list:
                bot.send_message(chat_id, f'Shit! {which_button} осталось всего {all_sold["All"]} !')

        elif all_sold['Sold_All'] == 1:
            bot.send_message(call.message.chat.id, sold_all_info_message.format(all_sold['Sold_All'],
                                                                                'шеврон', all_sold['All']))
        elif all_sold['Sold_All'] in (2, 3, 4):
            bot.send_message(call.message.chat.id, sold_all_info_message.format(all_sold['Sold_All'],
                                                                                'шеврона', all_sold['All']))
        else:
            bot.send_message(call.message.chat.id, sold_all_info_message.format(all_sold['Sold_All'],
                                                                                    'шевронов', all_sold['All']))
    except Exception as e:
        print("----exception----")
        print(e)
        print("----exception----")


def add_new_chevrons(message):
    try:
        print("new")
        count = int(message.text)

        if count > 50:
            bot.send_message(message.chat.id, "Не переходи границы!")
        else:
            new_value = db.add_new_chevrons_in_all_chevrons(chevron_name=which_button, count=count)
            bot.send_message(message.chat.id, f'Окей, добавляем {which_button}: {count}шт.')

            bot.send_message(message.chat.id, f'Было {new_value[0]}, теперь {new_value[1]}')

    except:
        bot.send_message(message.chat.id, "Ты ввёл не число, теперь всё по новой :(")


def update_price(message):
    try:
        print("new")

        new_price = int(message.text)

        new_value = db.update_price(chevron_name=which_button, new_price=new_price)
        bot.send_message(message.chat.id, f'Было {new_value[0]}, теперь {new_value[1]}')

    except:
        bot.send_message(message.chat.id, "Ты ввёл не число, теперь всё по новой :(")


bot.polling(none_stop=True)
