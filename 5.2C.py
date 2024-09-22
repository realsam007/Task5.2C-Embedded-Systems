import RPi.GPIO as GPIO
import tkinter as tk

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red_pin = 17
green_pin = 27
yellow_pin = 22

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)

# Setup PWM on each pin with a frequency of 1000 Hz
red_pwm = GPIO.PWM(red_pin, 1000)
green_pwm = GPIO.PWM(green_pin, 1000)
yellow_pwm = GPIO.PWM(yellow_pin, 1000)

# Start PWM with 0 duty cycle (LEDs off)
red_pwm.start(0)
green_pwm.start(0)
yellow_pwm.start(0)

# Function to update the PWM duty cycle for each LED
def update_red(val):
    red_pwm.ChangeDutyCycle(int(val))

def update_green(val):
    green_pwm.ChangeDutyCycle(int(val))

def update_yellow(val):
    yellow_pwm.ChangeDutyCycle(int(val))

# Tkinter GUI setup
root = tk.Tk()
root.title("LED Brightness Control")

# Sliders for LED brightness
tk.Label(root, text="Red LED Brightness").pack()
red_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_red)
red_slider.pack()

tk.Label(root, text="Green LED Brightness").pack()
green_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_green)
green_slider.pack()

tk.Label(root, text="Yellow LED Brightness").pack()
yellow_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_yellow)
yellow_slider.pack()

# Exit button
tk.Button(root, text="Exit", command=root.quit).pack()

# Main event loop
root.mainloop()

# Cleanup GPIO on exit
red_pwm.stop()
green_pwm.stop()
yellow_pwm.stop()
GPIO.cleanup()
