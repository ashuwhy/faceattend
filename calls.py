from serial import Serial
import time

# open a serial connection

# call the function
def present():
    s = Serial("COM5", 115200)
    print(s)
    while True:
        s.write(b"on\n")
        time.sleep(5)
        quit()