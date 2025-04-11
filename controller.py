heating_manual = None      # Користувач: True / False / None
heating_timer_force = None # Таймер: True / False / None

def control_heating(temp, threshold=20.0):
    global heating_manual, heating_timer_force

    if heating_manual is not None:
        return "Manual ON 🔥" if heating_manual else "Manual OFF ❄️"
    if heating_timer_force is not None:
        return "Timer ON ⏰🔥" if heating_timer_force else "Timer OFF ⏰❄️"

    return "Heating ON 🔥" if temp < threshold else "Heating OFF ❄️"

def set_manual(state):  # Користувач: True / False / None
    global heating_manual
    heating_manual = state

def set_timer(state):   # Таймер: True / False
    global heating_timer_force
    heating_timer_force = state
    print(f"[TIMER] Heating {'ENABLED' if state else 'DISABLED'}")
