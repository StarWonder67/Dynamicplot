import csv
import random
from itertools import count
import time
x = 0
y1 = random.uniform(0, 24)
y2 = random.uniform(0, 2)
y3 = random.uniform(0, 74)
y4 = random.uniform(0, 14)
y5 = random.uniform(0, 29)
y6 = random.uniform(0, 22)
y7 = random.uniform(0, 8)
y8 = random.uniform(0, 4)

fieldnames = ["x", "y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8"]

index = count()

with open('data1.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    while next(index) < 100:

            info = {
                "x": x,
                "y1": y1,
                "y2": y2,
                "y3": y3,
                "y4": y4,
                "y5": y5,
                "y6": y6,
                "y7": y7,
                "y8": y8
            }
            csv_writer.writerow(info)
            # print(x_value, y_value)

            x += 1
            y1 += random.uniform(-5, 10)
            y2 += random.uniform(-14, 13)
            y3 += random.uniform(-10, 17)
            y4 += random.uniform(-7, 10)
            y5 += random.uniform(-5, 12)
            y6 += random.uniform(-16, 16)
            y7 += random.uniform(-5, 6)
            y8 += random.uniform(-9, 9)

csv_file.close()
time.sleep(1)
