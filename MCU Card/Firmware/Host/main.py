from machine import UART, Pin, Timer
import utime, time

# Interrupt handler to ensure that we service ANY incoming UART data ASAP.
# This interrupt with its multiple calls to string functions takes about 31 ticks to complete, meaning that
# if data arrives faster than that, the UART handler will starve the rest of the microcontroller to the point
# of stalling.
def uart_handler(int):
    global time_dev1, time_dev2
    inttime = time.ticks_ms()
    received_data = uart.read().decode('utf-8')
    if(received_data[0:4] == "DEV1"):        
        print("Received: {", received_data, "} from DEV1 in", time.ticks_diff(inttime, time_dev1), "ms")
    print("Interrupt completed in", time.ticks_diff(time.ticks_ms(), inttime), "ticks")

# 9600 baud, UART0, GP16 (TX), GP17 (RX)
uart = machine.UART(0, baudrate=9600, tx=16, rx=17);
uart.irq(handler=uart_handler, trigger=UART.IRQ_RXIDLE, hard=0)

# Basic while loop handles polling
while True:
    utime.sleep_ms(10)
    time_dev1 = time.ticks_ms()
    uart.write("DEV1,LEDTOGGLE")
    #print("Polling DEV1")
    utime.sleep_ms(20)
    time_dev2 = time.ticks_ms()
    uart.write("DEV2")
    #print("Polling DEV2")
    utime.sleep_ms(15)		#this must be 13 or higher to avoid the uart handler triggering twice. Ideally 15.

