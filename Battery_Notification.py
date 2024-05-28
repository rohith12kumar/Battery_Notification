import psutil
from pynotifier import Notification

# Get battery information
battery = psutil.sensors_battery()
if battery is None:
    print("Cannot access battery information. Ensure the system supports battery monitoring.")
else:
    plugged = battery.power_plugged
    percent = battery.percent

    print(f"Battery percentage: {percent}%")
    print(f"Power plugged in: {plugged}")

    if percent <= 25 and not plugged:
        Notification(
            title="Battery Low",
            description=f"{percent}% Battery remaining!",
            duration=5,  # Duration in seconds
        ).send()
        print("Notification sent.")
    else:
        print("Battery status is adequate or charging.")
