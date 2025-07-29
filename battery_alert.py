import psutil
import subprocess
import time

def send_alert(title, message):
    subprocess.run(["notify-send", title , message])
    subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"])

last_alert = None 

while True:
    battery = psutil.sensors_battery()

    if battery is None:
        print("Battery info unavailable.")
        time.sleep(60)
        continue

    if(battery.power_plugged ==  True and battery.percent >= 85 and last_alert!='unplug'):
        title = "Plug Out Charger"
        message = "Charge > 85%"
        send_alert(title, message)
        last_alert = "unplug"

    elif(battery.power_plugged ==  False and battery.percent <= 35 and last_alert!='plug'):
        title = "Plug In Charger"
        message = "Charge < 35%"
        send_alert(title, message)
        last_alert = "plug"

    elif 35 < battery.percent < 85:
        last_alert = None  

    time.sleep(60)
