import psutil
from .error import CreateError

def getBatteryInfoApi():
    # Call the cross-platform battery sensor method
    battery = psutil.sensors_battery()
    
    # Trigger the failsafe if no hardware battery or metric is detected
    if battery is None:
        failsafe()
        
    # If battery exists, extract and return data safely
    return {
        "isPluggedIn": battery.power_plugged,
        "batteryPercent": battery.percent,
        "secsLeftUntilDead": battery.secsleft
    }
        
def failsafe():
    # Crucial: You MUST use the 'raise' keyword to actually trigger an error
    raise CreateError(
        ValueError, 
        "The batteryInfoApi Failed Because of a Failsafe that Detected No Metrics Were Detected"
    )
