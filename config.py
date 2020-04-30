import db

token = '1157156456:AAGan3P8RYWNjMsnYdgPoZFFsSC2UybyVVU'
url = f'https://api.telegram.org/bot{token}'
users_names = ['ZOG666', 'Himi_Jendrix']

chat_id_zog_666 = db.select_chat_id(user_name=users_names[0])
chat_id_himi_jendrix = db.select_chat_id(user_name=users_names[1])

chat_id_list = [chat_id_zog_666, chat_id_himi_jendrix]

