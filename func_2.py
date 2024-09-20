from sqlalchemy import create_engine
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import json


def connect_db():
    with open('keys.json', 'r') as file:
        data = json.load(file)

    host, database = data['host'], data['database']

    connection_string = f'mssql+pyodbc://{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

    try:
        engine = create_engine(connection_string)
        print("Conexion exitosa")
    except Exception as e:
        print("Error al conectar")
    
    return engine

def get_data(engine,written_query):
    query = f"{written_query}"
    df = pd.read_sql(query, engine)
    engine.dispose() 
    return df


def clean_data(df):
    df = df.sort_values(by=['nombre_sede','fechahora'],ascending=True).reset_index(drop=True)
    df['fechahora'] = pd.to_datetime(df['fechahora'])
    return df

def connect_wsp():
    with open('keys.json', 'r') as file:
        data = json.load(file)
        
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--ignore-certificate-errors")
    edge_options.add_argument("--log-level=3")
    driver = webdriver.Edge(options=edge_options)
    
    driver.get('https://web.whatsapp.com/')
    sleep(60)
    titulo_chat = data['titulo_chat_2']

    try:
        # Intenta encontrar el chat por su título
        chat = driver.find_element(By.XPATH, f'//span[@title="{titulo_chat}"]')
        chat.click()
    except:
        # Si no se encuentra el chat, imprime un mensaje y maneja la excepción como desees
        print("No se encontró el chat con el título proporcionado.")
    return driver


def show_emoji(emoji,campo_texto):
    campo_texto.send_keys(f":{emoji}")
    campo_texto.send_keys(Keys.ENTER)
    campo_texto.send_keys(Keys.SPACE)

def show_txt(tipo,value,campo_texto, bool_sub=0):
    # Nombre de la sede
    if(bool_sub==1):
        campo_texto.send_keys(">")
        campo_texto.send_keys(Keys.SPACE)

    header = f"{tipo} {value}"
    campo_texto.send_keys(header)
    campo_texto.send_keys( Keys.SHIFT + Keys.ENTER)

def message_T(df,driver):
    campo_texto = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

    for id,row in df.iterrows():

        if((row['valor'] >= 24)):
            
            show_emoji("fire",campo_texto)
            show_txt("Temperatura","",campo_texto)
            show_txt("Sede: ",row['nombre_sede'].title(),campo_texto,1)
            show_txt("Zona: ",row['nombre_zona'].title(),campo_texto,1)
            show_txt("Valor: ",row['valor'],campo_texto,1)
            show_txt("Hora: ",row['fechahora'].strftime('%H:%M:%S'),campo_texto,1)
            campo_texto.send_keys( Keys.SHIFT + Keys.ENTER)
            boton_enviar = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            boton_enviar.click()

    
def message_H(df,driver):
    campo_texto = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

    for id,row in df.iterrows():

        if((row['valor'] >= 85)):
            show_emoji("dropl",campo_texto)
            show_txt("Humedad","",campo_texto)
            show_txt("Sede: ",row['nombre_sede'].title(),campo_texto,1)
            show_txt("Zona: ",row['nombre_zona'].title(),campo_texto,1)
            show_txt("Valor: ",row['valor'],campo_texto,1)
            show_txt("Hora: ",row['fechahora'].strftime('%H:%M:%S'),campo_texto,1)
            campo_texto.send_keys( Keys.SHIFT + Keys.ENTER)        
            boton_enviar = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            boton_enviar.click()