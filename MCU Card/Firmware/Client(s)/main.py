from machine import UART, Pin
import utime

# 9600 baud, UART0, GP16 (TX), GP17 (RX)
uart = machine.UART(0, baudrate=9600, tx=16, rx=17);
led = machine.Pin("LED", machine.Pin.OUT)

# simple test: receive LED toggle commands. replace "DEV1" with whichever device identifier you wish to use.
while True:    
    if uart.any():
        received_data = uart.read().decode('utf-8')
        split_data = received_data.split(',')
        print("Received: ", split_data)
        if (split_data[0] == "DEV1"):
            print("Device selected with DEV1.")
            uart.write("DEV1 RESPONSE: " + str(utime.time()))
            if (split_data[1] == "LEDTOGGLE"):
                led.toggle()
