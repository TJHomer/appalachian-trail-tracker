import machine
import time
import network
import socket
import esp


## Functions that connect to the internet to get latitude data

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    print('connecting to network\n')
    sta_if.active(True)
    sta_if.connect('<your_internet>', '<your_password>')


def http_get(url):
    entries = ''
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    time.sleep(5)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    buffer = s.recv(464)  # this is the http info that comes before the actual data you want
    for i in range(5):
        data = s.recv(750)
        if data:
            chunk = str(data)
            entries = entries + chunk
        else:
            break
    item_list = entries.split("\"")
    s.close()
    return (item_list)


def get_info_from_data():
    url = http_get('<your_tracking_website>')
    for i in range(len(url)):
        if '<your-title>' in url[i]:
            return float(url[i + 40])


## LED class that maps each LED to a range of latitudes

class LED(object):
    LED_list = []

    def __init__(self, value, lat_upper=None, lat_lower=None):
        self.value = 2 ** value
        self.lat_upper = lat_upper
        self.lat_lower = lat_lower
        self.LED_list.append(self)


led1 = LED(26, lat_upper=34.913198, lat_lower=34)
led2 = LED(27, lat_upper=35.295240, lat_lower=led1.lat_upper)
led3 = LED(28, lat_upper=35.677282, lat_lower=led2.lat_upper)
led4 = LED(29, lat_upper=35.059324, lat_lower=led3.lat_upper)
led5 = LED(30, lat_upper=36.441365, lat_lower=led4.lat_upper)
led6 = LED(31, lat_upper=37.015106, lat_lower=led5.lat_upper)
led7 = LED(17, lat_upper=37.397148, lat_lower=led6.lat_upper)
led8 = LED(18, lat_upper=37.588169, lat_lower=led7.lat_upper)
led9 = LED(19, lat_upper=37.874400, lat_lower=led8.lat_upper)
led10 = LED(20, lat_upper=38.256742, lat_lower=led9.lat_upper)
led11 = LED(21, lat_upper=38.734972, lat_lower=led10.lat_upper)
led12 = LED(22, lat_upper=39.213201, lat_lower=led11.lat_upper)
led13 = LED(23, lat_upper=39.786942, lat_lower=led12.lat_upper)
led14 = LED(9, lat_upper=40.265171, lat_lower=led13.lat_upper)
led15 = LED(10, lat_upper=40.551703, lat_lower=led14.lat_upper)
led16 = LED(11, lat_upper=40.441365, lat_lower=led15.lat_upper)
led17 = LED(12, lat_upper=41.220276, lat_lower=led16.lat_upper)
led18 = LED(13, lat_upper=41.602318, lat_lower=led17.lat_upper)
led19 = LED(14, lat_upper=42.176058, lat_lower=led18.lat_upper)
led20 = LED(15, lat_upper=42.654288, lat_lower=led19.lat_upper)
led21 = LED(1, lat_upper=43.228028, lat_lower=led20.lat_upper)
led22 = LED(2, lat_upper=43.610070, lat_lower=led21.lat_upper)
led23 = LED(3, lat_upper=44.088300, lat_lower=led22.lat_upper)
led24 = LED(4, lat_upper=44.662040, lat_lower=led23.lat_upper)
led25 = LED(5, lat_upper=45.140270, lat_lower=led24.lat_upper)
led26 = LED(6, lat_upper=45.522312, lat_lower=led25.lat_upper)
led27 = LED(7, lat_upper=46.000000, lat_lower=led26.lat_upper)


def led_on(lat_coord):
    for led in LED.LED_list:
        if led.lat_upper > lat_coord:
            if led.lat_lower <= lat_coord:
                return led.value


## Values and Functions related to outputting data from esp8266

pin0 = machine.Pin(14, machine.Pin.OUT)
pin1 = machine.Pin(15, machine.Pin.OUT)
pin2 = machine.Pin(0, machine.Pin.OUT)


def clear():
    pin0.value(0)
    pin1.value(0)
    pin2.value(0)
    for value in [1, 3, 7, 15, 31, 63, 127, 255]:
        bits = [value >> i & 0 for i in range(7, -1, -1)]
        for i in range(7, -1, -1):
            pin0.value(bits[i])
            pin1.value(1)
            pin1.value(0)
    pin2.value(1)
    pin2.value(0)


def set_pin(value):
    bits = [value >> i & 1 for i in range(32, -1, -1)]
    for i in range(31, -1, -1):
        pin0.value(bits[i])
        pin1.value(1)
        pin1.value(0)
    pin2.value(1)
    pin2.value(0)


## Run program
do_connect()
print('connected')
lat = get_info_from_data()
print(lat)
value = led_on(lat)
clear()
set_pin(value)

