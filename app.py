from flask import Flask, render_template, request, redirect
from sensor import get_all_sensors
from controller import control_heating, set_manual, set_timer
from apscheduler.schedulers.background import BackgroundScheduler
from models import Session, SensorLog
import datetime

app = Flask(__name__)

# Планировщик таймера
scheduler = BackgroundScheduler()
scheduler.start()

# Таймер включения/выключения отопления по расписанию
scheduler.add_job(lambda: set_timer(True), 'cron', hour=6, minute=0)    # Утреннее включение
scheduler.add_job(lambda: set_timer(True), 'cron', hour=18, minute=0)   # Вечернее включение
scheduler.add_job(lambda: set_timer(False), 'cron', hour=9, minute=0)   # Утреннее выключение
scheduler.add_job(lambda: set_timer(False), 'cron', hour=23, minute=0)  # Ночное выключение

# Главная страница
@app.route('/')
def index():
    data = get_all_sensors()
    status = control_heating(data["temperature"])
    return render_template("index.html", **data, status=status)

# Обработка кнопок управления (вкл/выкл/авто)
@app.route('/set/<state>')
def set_state(state):
    if state == "on":
        set_manual(True)
    elif state == "off":
        set_manual(False)
    elif state == "auto":
        set_manual(None)
    return redirect("/")

# Маршрут для получения данных с БД (для графика)
@app.route('/log')
def log():
    session = Session()
    logs = session.query(SensorLog).order_by(SensorLog.timestamp.desc()).limit(20).all()
    logs.reverse()
    data = {
        "temperatures": [log.temperature for log in logs],
        "humidity": [log.humidity for log in logs],
        "co2": [log.co2 for log in logs],
        "pressure": [log.pressure for log in logs],
        "timestamps": [log.timestamp.strftime("%H:%M") for log in logs]
    }
    session.close()
    return data

if __name__ == '__main__':
    app.run(debug=True)
