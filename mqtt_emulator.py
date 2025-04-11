import time
from sensor import get_temperature

# Просто имитируем передачу данных по MQTT (в лог)
while True:
    temp = get_temperature()
    print(f"[MQTT] Published temperature: {temp}°C")
    time.sleep(5)
