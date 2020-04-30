import sqlite3
import requests


users_names = ['ZOG666', 'Himi_Jendrix']

columns = ['MW', 'MW_Ветеран', 'Комплект_Воина', 'Арабский',
           'Русский', 'Quarantine', 'COVID_Ветеран', 'Комплект_Карантин']

list_chevrons = ['MW', 'MW_Ветеран', 'Арабский',
                 'Русский', 'Quarantine', 'COVID_Ветеран']

exchange_api = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
default_price = (200, 300, 450, 250, 150, 250, 250, 450)

complect_voin = [columns[0], columns[1]]
complect_quarantine = [columns[5], columns[6]]


def get_actual_exchange():
    r = requests.get(exchange_api)
    response = r.json()
    actual_exchange = response[2]['sale']

    return float(actual_exchange)


def get_connection():
    print('------')
    print('Trying to connection to database...')
    connection = sqlite3.connect('database.db')
    print('Success')
    return connection


def init_sold_chevrons_table(force=False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        print('Trying to delete sold_chevrons table')
        c.execute('DROP TABLE sold_chevrons')
        print('Done! Table sold_chevrons was deleted.')

    create_table = 'CREATE TABLE sold_chevrons (' \
                   'MW     INTEGER,' \
                   'MW_Ветеран INTEGER,'\
                   'Комплект_Воина INTEGER,'\
                   'Арабский INTEGER,'\
                   'Русский INTEGER,'\
                   'Quarantine INTEGER,'\
                   'COVID_Ветеран INTEGER,'\
                   'Комплект_Карантин INTEGER)'
    print('Trying to create sold_chevrons table..')
    c.execute(create_table)
    print('Done! Table was created.')
    print('Trying to set 0 value for all colunms..')
    c.execute(f'INSERT INTO sold_chevrons  VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (0, 0, 0, 0, 0, 0, 0, 0))
    conn.commit()
    print('Done! Table sold_chevrons successfully created!')
    conn.close()


def init_all_chevrons_table(force=False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        print('Trying to delete all_chevrons table')
        c.execute('DROP TABLE all_chevrons')
        print('Done! Table all_chevrons was deleted.')

    create_table = 'CREATE TABLE all_chevrons (' \
                   'MW     INTEGER,' \
                   'MW_Ветеран INTEGER,'\
                   'Арабский INTEGER,'\
                   'Русский INTEGER,'\
                   'Quarantine INTEGER,'\
                   'COVID_Ветеран INTEGER)'
    print('Trying to create all_chevrons table..')
    c.execute(create_table)
    print('Done! Table was created.')
    print('Trying to set 0 value for all colunms..')
    c.execute(f'INSERT INTO all_chevrons  VALUES (?, ?, ?, ?, ?, ?)', (0, 0, 0, 0, 0, 0))
    conn.commit()
    print('Done! Table all_chevrons successfully created!')
    conn.close()


def init_price_chevrons_table_and_set_default_price(force=False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        print('Trying to delete price_chevrons table')
        c.execute('DROP TABLE price_chevrons')
        print('Done! Table price_chevrons was deleted.')

    create_table = 'CREATE TABLE price_chevrons (' \
                   'MW     INTEGER,' \
                   'MW_Ветеран INTEGER,'\
                   'Комплект_Воина INTEGER,'\
                   'Арабский INTEGER,'\
                   'Русский INTEGER,'\
                   'Quarantine INTEGER,'\
                   'COVID_Ветеран INTEGER,'\
                   'Комплект_Карантин INTEGER)'
    print('Trying to create price_chevrons table..')
    c.execute(create_table)
    print('Done! Table was created.')
    print('Trying to set default_price value for all colunms..')
    c.execute(f'INSERT INTO price_chevrons  VALUES (?, ?, ?, ?, ?, ?, ?, ?)', default_price)
    conn.commit()
    print('Done! Table price_chevrons successfully created!')
    conn.close()


def init_chat_id_table(force=False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        print('Trying to delete chat_id table')
        c.execute('DROP TABLE chat_id')
        print('Done! Table chat_id was deleted.')

    create_table = 'CREATE TABLE chat_id (' \
                   f'{users_names[0]} INTEGER,' \
                   f'{users_names[1]} INTEGER)'

    print('Trying to create chat_id table..')
    c.execute(create_table)
    print('Done! Table was created.')
    print('Trying to set default value for all columns..')
    c.execute(f'INSERT INTO chat_id  VALUES (?, ?)', (805460958, 627847832))
    conn.commit()
    print('Done! Table chat_id successfully created!')
    conn.close()


def select_chat_id(user_name=None, logs=True):
    conn = get_connection()
    c = conn.cursor()

    if logs:
        print(f'Trying to get chat_id for {user_name if user_name else "all users"}')

    get_value = f'SELECT {user_name if user_name else "*"} FROM chat_id'
    results = c.execute(get_value).fetchall()
    result = list(results[0])
    if user_name:
        all_dict = result[0]
    else:
        all_dict = dict(zip(users_names, result))
    if logs:
        print(f'chat_id for {user_name if user_name else "all users"} = {all_dict}')
    conn.close()
    return all_dict


def update_chat_id(user_name=None, chat_id=0):
    conn = get_connection()
    c = conn.cursor()

    print(f'Trying to update chat_id {chat_id} for {user_name}')
    db_value = select_chat_id(user_name, logs=False)
    print(f'value in db = {db_value}')

    c.execute(f'UPDATE chat_id SET {user_name} = {chat_id}')

    print(f'Done. New value={chat_id} for {user_name} user')

    conn.commit()
    conn.close()


def select_from_all_chevrons(chevron_name=None):
    conn = get_connection()
    c = conn.cursor()

    get_value = f'SELECT {chevron_name if chevron_name else "*"} FROM all_chevrons'
    print(f"Trying to get value from db \nget value is:\n{get_value}")
    results = c.execute(get_value).fetchall()
    actual_value = list(results[0])

    if not chevron_name:
        all_dict = dict(zip(list_chevrons, actual_value))
    else:
        all_dict = actual_value
    print(f"Done. Actual value is\n{all_dict}")

    conn.close()
    print('Close connection')
    return all_dict


def select_from_sold_chevrons(chevron_name=None):
    conn = get_connection()
    c = conn.cursor()

    get_value = f'SELECT {chevron_name if chevron_name else "*"} FROM sold_chevrons'
    print(f"Trying to get value from db \nget value is:\n{get_value}")
    results = c.execute(get_value).fetchall()
    actual_value = list(results[0])

    if not chevron_name:
        all_dict = dict(zip(columns, actual_value))
    else:
        all_dict = actual_value
    print(f"Done. Actual value is\n{all_dict}")

    conn.close()
    print('Close connection')
    return all_dict


def add_sold_value(chevron_name):
    print("Trying to add 1 sold chevron")
    conn = get_connection()
    c = conn.cursor()

    print(f"Trying to get actual value {chevron_name}")

    get_value = f'SELECT {chevron_name} FROM sold_chevrons'
    results = c.execute(get_value).fetchall()
    actual_value = results[0][0]
    print(f'Actual value for {chevron_name} = {actual_value}')

    get_value_in_all_chevrons = f'SELECT {chevron_name} FROM all_chevrons'
    results_all = c.execute(get_value_in_all_chevrons).fetchall()
    actual_value_in_all_chevrons = results_all[0][0]
    print(f'Actual value ALL CHEVRONS! {chevron_name} = {actual_value_in_all_chevrons}')

    actual_value += 1
    actual_value_in_all_chevrons -= 1

    print(f'Trying to update {chevron_name} = {actual_value}')

    c.execute(f'UPDATE sold_chevrons SET {chevron_name} = {actual_value}')
    c.execute(f'UPDATE all_chevrons SET {chevron_name} = {actual_value_in_all_chevrons}')
    sold_all = c.execute(get_value).fetchall()[0][0]
    all_chevrons = c.execute(get_value_in_all_chevrons).fetchall()[0][0]

    conn.commit()

    print(f"Done! {chevron_name} = {sold_all}")
    print(f"All {chevron_name} = {all_chevrons}")
    print('------')
    all_info = {"Sold_All": sold_all, "All": all_chevrons}
    conn.close()
    return all_info


def correct_sold_value(chevron_name):
    print("Trying to delete 1 sold chevron")
    conn = get_connection()
    c = conn.cursor()

    print(f"Trying to get actual value {chevron_name}")

    get_value = f'SELECT {chevron_name} FROM sold_chevrons'
    results = c.execute(get_value).fetchall()
    actual_value = results[0][0]
    print(f'Actual value for {chevron_name} = {actual_value}')

    get_value_in_all_chevrons = f'SELECT {chevron_name} FROM all_chevrons'
    results_all = c.execute(get_value_in_all_chevrons).fetchall()
    actual_value_in_all_chevrons = results_all[0][0]
    print(f'Actual value ALL CHEVRONS! {chevron_name} = {actual_value_in_all_chevrons}')

    actual_value -= 1
    actual_value_in_all_chevrons += 1

    print(f'Trying to update {chevron_name} = {actual_value}')

    c.execute(f'UPDATE sold_chevrons SET {chevron_name} = {actual_value}')
    c.execute(f'UPDATE all_chevrons SET {chevron_name} = {actual_value_in_all_chevrons}')
    sold_all = c.execute(get_value).fetchall()[0][0]
    all_chevrons = c.execute(get_value_in_all_chevrons).fetchall()[0][0]

    conn.commit()

    print(f"Done! {chevron_name} = {sold_all}")
    print(f"All {chevron_name} = {all_chevrons}")
    print('------')
    all_info = {"Sold_All": sold_all, "All": all_chevrons}
    conn.close()
    return all_info


def add_sold_complect_value(complect_name=None):
    print("Trying to add 1 sold complect")
    conn = get_connection()
    c = conn.cursor()

    get_value = f'SELECT {complect_name} FROM sold_chevrons'
    results = c.execute(get_value).fetchall()
    actual_value = results[0][0]
    print(f'Actual value for {complect_name} is {actual_value}')
    actual_value += 1

    c.execute(f'UPDATE sold_chevrons SET {complect_name} = {actual_value}')
    results = c.execute(get_value).fetchall()
    new_sold = results[0][0]

    if complect_name == 'Комплект_Воина':
        complect = complect_voin
    else:
        complect = complect_quarantine

    value0 = select_from_all_chevrons(complect[0])[0]
    value1 = select_from_all_chevrons(complect[1])[0]

    value0 -= 1
    value1 -= 1

    c.execute(f'UPDATE all_chevrons SET {complect[0]} = {value0}')
    c.execute(f'UPDATE all_chevrons SET {complect[1]} = {value1}')

    conn.commit()
    new_value = select_from_all_chevrons(f'{complect[0]}, {complect[1]}')
    result = {complect_name: new_sold,
              complect[0]: new_value[0],
              complect[1]: new_value[1]}
    conn.close()
    print(result)
    return result


def correct_sold_complect_value(complect_name=None):
    print("Trying to add 1 sold complect")
    conn = get_connection()
    c = conn.cursor()

    get_value = f'SELECT {complect_name} FROM sold_chevrons'
    results = c.execute(get_value).fetchall()
    actual_value = results[0][0]
    print(f'Actual value for {complect_name} is {actual_value}')
    actual_value -= 1

    c.execute(f'UPDATE sold_chevrons SET {complect_name} = {actual_value}')
    results = c.execute(get_value).fetchall()
    new_sold = results[0][0]

    if complect_name == 'Комплект_Воина':
        complect = complect_voin
    else:
        complect = complect_quarantine

    value0 = select_from_all_chevrons(complect[0])[0]
    value1 = select_from_all_chevrons(complect[1])[0]

    value0 += 1
    value1 += 1

    c.execute(f'UPDATE all_chevrons SET {complect[0]} = {value0}')
    c.execute(f'UPDATE all_chevrons SET {complect[1]} = {value1}')

    conn.commit()
    new_value = select_from_all_chevrons(f'{complect[0]}, {complect[1]}')
    result = {complect_name: new_sold,
              complect[0]: new_value[0],
              complect[1]: new_value[1]}
    conn.close()
    print(result)
    return result


def add_new_chevrons_in_all_chevrons(chevron_name, count=0):
    print("Trying to add new chevron")
    conn = get_connection()
    c = conn.cursor()

    print(f"Trying to get actual value {chevron_name}")

    get_value = f'SELECT {chevron_name} FROM all_chevrons'
    results = c.execute(get_value).fetchall()
    old_value = results[0][0]

    print(f'Actual value for {chevron_name} = {old_value}')

    new_value = old_value + count

    print(f'Trying to update {chevron_name} = {new_value}')

    c.execute(f'UPDATE all_chevrons SET {chevron_name} = {new_value}')
    new_value = c.execute(get_value).fetchall()[0][0]
    conn.commit()

    print(f"Done! {chevron_name} = {new_value}")
    print('------')

    conn.close()
    return old_value, new_value


def set_0_value_in_sold_table():
    conn = get_connection()
    c = conn.cursor()

    print('Trying to SET 0 values in sould_chevrons table')
    for name in columns:
        c.execute(f'UPDATE sold_chevrons SET {name} = 0')
    conn.commit()
    print('Done')
    conn.close()


def get_price(chevron_name=None):
    conn = get_connection()
    c = conn.cursor()

    get_value = f'SELECT {chevron_name if chevron_name else "*"} FROM price_chevrons'
    print(f"Trying to get value from db \nget value is:\n{get_value}")
    results = c.execute(get_value).fetchall()
    actual_value = list(results[0])

    if not chevron_name:
        all_dict = dict(zip(columns, actual_value))
    else:
        all_dict = actual_value
    print(f"Done. Actual price is\n{all_dict}")

    conn.close()
    print('Close connection')

    return all_dict


def update_price(chevron_name, new_price=0):
    print("Trying to add new chevron")
    conn = get_connection()
    c = conn.cursor()

    print(f"Trying to get actual value {chevron_name}")

    old_value = get_price(chevron_name)[0]

    print(f'Trying to update {chevron_name} = {new_price}')

    c.execute(f'UPDATE price_chevrons SET {chevron_name} = {new_price}')
    conn.commit()

    new_value = get_price(chevron_name)[0]
    print(f"Done! {chevron_name} = {new_value}")
    print('------')

    conn.close()
    return old_value, new_value


def main_report():
    price = get_price()
    all_sold = select_from_sold_chevrons()

    numbers_of_chevrons = 0
    for count in all_sold.values():
        numbers_of_chevrons = numbers_of_chevrons+count

    all_count = {"All_count": numbers_of_chevrons}

    all_mw_money =               price[columns[0]] * all_sold[columns[0]]
    all_mw_veter_money =         price[columns[1]] * all_sold[columns[1]]
    all_mw_comp_money =          price[columns[2]] * all_sold[columns[2]]
    all_arab_money =             price[columns[3]] * all_sold[columns[3]]
    all_russ_money =             price[columns[4]] * all_sold[columns[4]]
    all_quarantine_money =       price[columns[5]] * all_sold[columns[5]]
    all_covid_veter_money =      price[columns[6]] * all_sold[columns[6]]
    all_quarantine_comp_money =  price[columns[7]] * all_sold[columns[7]]

    all_money_rub ={'All_money_rub': all_mw_money + all_mw_veter_money + all_mw_comp_money + all_arab_money
                                     + all_russ_money + all_quarantine_money + all_covid_veter_money
                                     + all_quarantine_comp_money}

    details = {
        columns[0]: all_mw_money,
        columns[1]: all_mw_veter_money,
        columns[2]: all_mw_comp_money,
        columns[3]: all_arab_money,
        columns[4]: all_russ_money,
        columns[5]: all_quarantine_money,
        columns[6]: all_covid_veter_money,
        columns[7]: all_quarantine_comp_money
    }

    return details, all_money_rub, all_count
