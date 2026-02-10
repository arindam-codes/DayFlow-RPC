## a time aware discord rich presence that reflects your daily rhythm
## First real world project after MIT 6.100L

## Libraries 
from pypresence import Presence
from pypresence.types import *
from datetime import datetime
import time
import math

## Current time
def get_time_value():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    time_value = hour + (minute / 60.0)
    return time_value

## Defining modes
class Mode:
    
    """creates modes"""
    
    def __init__(self, icon=None, status=None, end_time=0, name=None, state=None, details=None, next_task=None):
        self.icon = icon
        self.status = status
        self.end_time = end_time
        self.name = name
        self.state = state
        self.details = details
        self.next_task = next_task
    
deep_focus = Mode(
    icon="deep_focus",
    status="grinding_status",
    end_time=11,
    name="Deep Focus 🚀",
    details="Morning deep-focus session 🌅",
    state=f"Guitar 🎸 in next",
    )

guitar_practice = Mode(
    icon="guitar_icon",
    status="guitar_status",
    end_time=12,
    name="Guitar Practice 🎸",
    details="Creative Session",
    state=f"study block in next"
    )

growth = Mode(
    icon="growth_mode_icon",
    status="growth_mode_status",
    end_time=16,
    name="Mission Mode: Growth 🧠",
    details="Back in deep focus — building step by step",
    state=f"chill time 🍿 in next"
    )

chill_time = Mode(
    icon="chill_time_icon",
    status="chill_time_status",
    end_time=16.5,
    name="Chill Time 🍿",
    details="Calm time before getting back to work",
    state=f"Final Focus Sprint 🔒 in next"
    )

final_Focus_Sprint = Mode(
    icon="final_focus_sprint_icon",
    status="final_focus_sprint_status",
    end_time=18,
    name="Final Focus Sprint 🔒",
    details="Back into focus till 6",
    state=f"Documentation work in next"
    )

documentation = Mode(
    icon="documentation_icon",
    status="documentation_status",
    end_time=18.5,
    name="Progress Review & Notes",
    details="Documenting today's work and organizing progress",
    state=f"Reset & Get Ready in next"
    )

gym_prep = Mode(
    icon="gym_prep_icon",
    status="gym_prep_status",
    end_time=19,
    name="Reset & Get Ready 💪",
    details="Getting ready for the gym — switching gears 💪",
    state=f"Gym starting 🏋️‍♂️ in next"
    )

gym = Mode(
    icon="gym_icon",
    status="gym_status",
    end_time=21.5,
    name="Training for Strength 🏋️‍♂️",
    details="Gym session — pushing limits and staying focused 💪",
    state=f"Unwind & Reset in next"
    )

unwind_reset = Mode(
    icon="day_end_icon",
    status="day_end_status",
    end_time=23,
    name="Unwind & Reset",
    details="The Soul needs Rest",
    state=f"Post-workout, bath, end of today's era in"
    )

sleep = Mode(
    icon="sleep_icon",
    end_time=6,
    name="Sleep",
    details="Sleeping bruh 💤",
    state=f"Wake up at 6 AM",
    )

## Choosing the current_mode
def mode_checker():    
    
    time_value = get_time_value()

    if 6 <= time_value < 11:
        return deep_focus 
    elif 11 <= time_value < 12:
        return guitar_practice
    elif 12 <= time_value < 16:
        return growth
    elif 16 <= time_value < 16.5:
        return chill_time 
    elif 16.5 <= time_value < 18:
        return final_Focus_Sprint
    elif 18 <= time_value < 18.5:
        return documentation
    elif 18.5 <= time_value < 19:
        return gym_prep
    elif 19 <= time_value < 21.5:
        return gym
    elif 21.5 <= time_value < 23:
        return unwind_reset
    else:
        return sleep


## getting the time left for the next current_mode
def time_left(current_mode):
    now = get_time_value()
    end = current_mode.end_time
    if end >= now:
        time_left = end - now
    else:
        time_left = (24 - now) + end
    integer_part = math.floor(time_left)
    decimal_part = time_left - integer_part
    hour, minute = integer_part, int(decimal_part * 60)
    return hour, minute

## creating rich presence object
rpc = Presence(1470375444376326266)

## waiting to open local discord app
while True:
    try:
        rpc.connect()
        print("Connected to Discord RPC")
        break
    except Exception:
        print("Waiting for Discord ... ")
        time.sleep(5)

while True:
    
    current_mode = mode_checker()
    hour_left, minute_left = time_left(current_mode)

    ## Checking if its sleeping time
    if current_mode is sleep:
        rpc.update(

            large_image=current_mode.icon,
            name=current_mode.name,
            details=current_mode.details,
            state=current_mode.state
        )
    else:
        rpc.update(
            
            large_image=current_mode.icon,
            small_image=current_mode.status,
            name= current_mode.name,
            details=current_mode.details,    
            state=f"{current_mode.state} {hour_left} hrs : {minute_left} mins"
        )
    time.sleep(120)
