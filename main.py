import time
import machine
import network

ssid_ = "JioFi3_67EC0B"
wp2_pass = "nf6x676kc4"


sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
sta_if.connect(ssid_, wp2_pass)

led = machine.Pin(2,machine.Pin.OUT)

while True:
    print ('Oyyyy')
    led.value(not led.value())
    time.sleep(0.15)