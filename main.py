# main.py -- put your code here!
import dht, machine,pyb, time


X2 = pyb.Pin('X2',pyb.Pin.ANALOG)

d = dht.DHT22(machine.Pin('X1'))
adcx2 = pyb.ADC(X2)
sw = pyb.Switch()

start = time.ticks_ms()
button = True


m = []
t = []
h = []
l = []

while button:
    pyb.LED(4).on()
    # keep track of time
    delta = time.ticks_diff(time.ticks_ms(), start)
    minutes = delta / 1000 / 60
    

    #temp and humidity
    d.measure()
    temp = round(d.temperature() * 1.8 + 32,2)
    humidity = round(d.humidity(),2)
        
    # light is measure 0 to 10 scale 0 being none
    # and 10 being the most 
    light = adcx2.read() / 4095 * 10

    # append lists
    m.append(minutes)
    t.append(temp)
    h.append(humidity)
    l.append(light)

    #delay
    pyb.delay(150000)
    pyb.LED(4).off()
    pyb.LED(3).on()
    pyb.delay(150000)
    pyb.LED(3).off()

    if sw.value() == True:
        button = False

#save data
log = open('log.csv','w')
for i in range(len(m)):
    log.write('{}|{}|{}|{} \n'.format(m[i],t[i],h[i],l[i]))
pyb.LED(4).off()
log.close()
    

