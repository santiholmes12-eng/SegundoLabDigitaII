#Codigo para medir temperatura y humedad con el sensor DHT11 ESP32.
from machine import Pin 
from time import sleep 
import dht 

sensor = dht.DHT11(Pin(4))

while True:

    sensor.measure()
    temperatura = sensor.temperature()
    humumedad = sensor.humidity()
    print("Temperatura " + str(temperatura) + "°C Y Humedad " + str(humumedad) + "%")
    sleep(2)
    