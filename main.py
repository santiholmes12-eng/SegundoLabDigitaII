'''#Codigo para medir temperatura y humedad con el sensor DHT11 ESP32.
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
    '''
    
'''#Codigo para servomotor con ESP32
import machine
import time

p19 = machine.Pin(19, machine.Pin.OUT)
pwm = machine.PWM(p19)
pwm.freq(50)

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def mover_servo(angulo):
    duty = map(angulo, 0, 180, 20, 120)
    pwm.duty(duty)

# Inicializacion
mover_servo(0)
time.sleep(0.5)

# Barrido inicial
for i in range(0, 181, 10):
    mover_servo(i)
    time.sleep(0.5)

# Sigue preguntando indefinidamente
while True:
    ang = int(input("Angulo (0-180): "))
    mover_servo(ang)
    time.sleep(0.5)'''

'''#Codigo para matriz de led 8x32
import max7219
from machine import Pin, SPI
from time import sleep

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 4)

mensaje = 'Este proyecto me lo voy a sacar en 5.0 '

while True:
    for i in range(len(mensaje) * 8 + 32):
        display.fill(0)
        display.text(mensaje, 32 - i, 0, 1)
        display.show()
        sleep(0.05)
    '''

# Conexion WiFi y sincronizacion de hora.
import network
from time import sleep
import ntptime
import time

# Conexion WiFi (ya la tienes)
MiWIFI = network.WLAN(network.STA_IF)
MiWIFI.active(False)
sleep(1)
MiWIFI.active(True)
sleep(2)
MiWIFI.disconnect()
sleep(1)
MiWIFI.connect("APARTAMENTO ", "apto3623")

while not MiWIFI.isconnected():
    sleep(1)

print("Conectado!")

# Sincronizar hora
ntptime.settime()

# Ajustar a hora colombiana UTC-5
UTC_OFFSET = -5 * 3600

while True:
    hora_actual = time.time() + UTC_OFFSET
    t = time.localtime(hora_actual)
    
    fecha = "{:02d}/{:02d}/{:04d}".format(t[2], t[1], t[0])
    hora = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])
    
    print("Fecha: " + fecha + "  Hora: " + hora)
    sleep(1)
