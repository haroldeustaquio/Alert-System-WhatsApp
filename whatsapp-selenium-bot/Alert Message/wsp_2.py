from func_2 import *

driver = connect_wsp()

while True:

    engine = connect_db()
    df = get_data(engine,"select * from last_update_T where nombre_alternativo  like 'AOC2'")
    df = clean_data(df)
    message_T(df,driver)

    sleep(15)

    engine = connect_db()
    df = get_data(engine,"select * from last_update_H where nombre_alternativo  like 'AOC2'")
    df = clean_data(df)
    message_H(df,driver)
    sleep(60)