import csv
import random
import time
import collections
import math
x_value = 0
temp = random.randint(0, 24)
pressure = random.randint(0, 2)
speed = random.randint(0, 10)
rotation = random.randint(0, 15)
height = random.randint(0, 17)
rnge = random.randint(0, 5)
humidity = random.randint(0, 9)
momentum = random.randint(0, 2)


de = collections.deque([0])

fieldnames = ["x_value", "temp","pressure","speed","rotation","height","rnge","humidity","momentum"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": de[-1],
            "temp": temp,
            "pressure": pressure,
            "speed": speed,
            "rotation": rotation,
            "height": height,
            "rnge": rnge,
            "humidity": humidity,
            "momentum": momentum

        }

        csv_writer.writerow(info)

        x_value = (x_value+1)%100
        
        temp = temp + random.randint(-5, 10)
        pressure = pressure +  random.randint(-5, 10)
        speed = speed + math.sqrt(2*10*height)
        rotation = rotation + random.randint(0, 60)

        height = height + 10

        rnge = rnge + random.randint(-10, 7)

        humidity = humidity + random.randint(-5, 25)

        momentum= momentum + random.randint(-1, 10)

        print(x_value, temp,pressure,speed,rotation,height,rnge,humidity,momentum)
       
        

    time.sleep(1)