from gpiozero import PWMLED
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from time import sleep
from signal import pause

#gpio16 = LED(16)
#gpio13 = LED(13)
pwm = PWMLED(12)
#while True:
 #   red.on()
  #  sleep(1)
   # red.off()
    #sleep(1)

app = FastAPI()

def speed_step(start, finish):
    # determine the difference between the start and finish speeds and reduce the difference by 0.1 each 500ms until finish speed is reached
    step = 0.1 if start < finish else -0.1
    sequence = []
    speed = start
    while (speed <= finish) if step > 0 else (speed >= finish):
        pwm.value = float(f"{speed:.1f}")
        sleep(0.5)  # 500ms delay
        speed += step
    return

@app.get("/on")
async def on():
    #gpio16.on()
    return {"message" : "turning on pin 36, GPIO 16"}

@app.get("/off")
async def off():
    #gpio16.off()
    return {"message" : "turning off pin 36, GPIO 16"}

@app.get("/speed")
async def speed(value: float = 0.5):
    start = pwm.value
    finish = value
    print(f"here is value {pwm.value}")
    speed_step(start, finish)
    return {"message" : "pulsing pin 36, GPIO 16"}

@app.get("/speedUp")
async def speedup(value: float = 0.05):
    if pwm.value >= 0.95:
        pwm.value = 1
        return {"message" : f"speed increased by {value}, new speed {pwm.value}"}
    pwm.value = pwm.value + 0.05
    print(f"here is value {pwm.value}")
    return {"message" : f"speed increased by {value}, new speed {pwm.value}"}

@app.get("/speedDown")
async def speeddown(value: float = 0.05):
    if pwm.value <= 0.05:
        pwm.value = 0
        return {"message" : f"speed decreased by {value}, new speed {pwm.value}"}
    pwm.value = pwm.value - 0.05
    print(f"here is value {pwm.value}")
    return {"message" : f"speed decreased by {value}, new speed {pwm.value}"}

app.mount("/home", StaticFiles(directory="static"), name ="static")
