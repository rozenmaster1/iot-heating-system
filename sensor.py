import random
from datetime import datetime
from models import SensorLog, Session

def get_temperature():
    return round(random.uniform(15.0, 25.0), 2)

def get_humidity():
    return round(random.uniform(30.0, 70.0), 2)

def get_co2():
    return round(random.uniform(400, 1200), 0)

def get_pressure():
    return round(random.uniform(980, 1040), 2)

def get_all_sensors():
    temp = get_temperature()
    hum = get_humidity()
    co2 = get_co2()
    pres = get_pressure()

    # Сохраняем в базу данных
    session = Session()
    log = SensorLog(
        temperature=temp,
        humidity=hum,
        co2=co2,
        pressure=pres
    )
    session.add(log)
    session.commit()
    session.close()

    return {
        "temperature": temp,
        "humidity": hum,
        "co2": co2,
        "pressure": pres
    }
