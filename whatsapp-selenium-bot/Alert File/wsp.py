from func import *

driver = connect_wsp()

def all_process():
    data = []
    warning = 0
    alert = 0

    engine = connect_db()
    df = get_data(engine,"select * from last_update_T where nombre_alternativo  like 'AOC2'")
    df = clean_data(df)
    data, warning, alert = message_T(df,data,warning,alert)
    
    sleep(15)
    
    engine = connect_db()
    df = get_data(engine,"select * from last_update_H where nombre_alternativo  like 'AOC2'")
    df = clean_data(df)
    data, total = message_H(df,driver,data,warning,alert)
    
    if total != 0:
        send_excel(driver,data)

at_hour(all_process)
