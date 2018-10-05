import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging


def fetch_data():

    url = 'https://api.openweathermap.org/data/2.5/weather?' + 'q=London,uk' + '&appid=19c71fe86672dae33dfeb941c79ab379&units=metric'
    r = requests.get(url).json()
    data = r['main']

    temp = data['temp']
    temp_min = data['temp_min']
    temp_max = data['temp_max']
    pressure = data['pressure']
    humidity = data['humidity']
    last_update = datetime.now()


    try:
        conn = psycopg2.connect(dbname='weather', user='postgres', password='P@$$word', host='localhost')
        print('opened db!')
    except:
        print(datetime.now(),'unable to connect')
        logging.exception('unable to connect')
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    cur.execute("""INSERT INTO station_reading(temp, temp_min, temp_max, pressure, humidity, last_update)
     VALUES(%s,%s,%s,%s,%s,%s)""", (temp, temp_min, temp_max, pressure, humidity, last_update))

    conn.commit()
    cur.close()
    conn.close()

    print('data inserted', datetime.now())


fetch_data()
