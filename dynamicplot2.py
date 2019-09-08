import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count(0, 100)

lb = count(0, 2)
ub = count(10, 2)

lb2 = count(0, 2)
ub2 = count(10, 2)

lb3 = count(0, 2)
ub3 = count(10, 2)

lb4 = count(0, 2)
ub4 = count(10, 2)

lb5 = count(0, 2)
ub5 = count(20, 2)
lb6 = count(0, 2)
ub6 = count(20, 2)

lb7 = count(0, 2)
ub7 = count(20, 2)

lb8 = count(0, 2)
ub8 = count(20, 2)

fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8]) = plt.subplots(nrows=4, ncols=2)

while True:

    def animate(i):

        data = pd.read_csv('data1.csv')
        x = data['x']  # + next(index)
        y1 = data['y1']
        y2 = data['y2']
        y3 = data['y3']
        y4 = data['y4']
        y5 = data['y5']
        y6 = data['y6']
        y7 = data['y7']
        y8 = data['y8']

        ax1.cla()
        ax1.plot(x, y1, label='temp vs time')
        ax1.set_xlabel("Time(s)")
        ax1.set_ylabel('Temp(Degree C)')
        ax1.set_xbound(next(lb), next(ub))

        ax2.cla()
        ax2.plot(x, y2, label='pressure vs time')
        ax2.set_xlabel("Time(s)")
        ax2.set_ylabel("Pressure(atm)")
        ax2.set_xbound(next(lb2), next(ub2))

        ax3.cla()
        ax3.plot(x, y3, label='Speed vs time')
        ax3.set_xlabel("Time(s)")
        ax3.set_ylabel('Speed(m/s)')
        ax3.set_xbound(next(lb3), next(ub3))

        ax4.cla()
        ax4.plot(x, y4, label='rotation vs time')
        ax4.set_xlabel("Time(s)")
        ax4.set_ylabel('rotation(rad/s)')
        ax4.set_xbound(next(lb4), next(ub4))

        ax5.cla()
        ax5.plot(x, y5, label='height vs time')
        ax5.set_xlabel("Time(s)")
        ax5.set_ylabel('height(m)')
        ax5.set_xbound(next(lb5), next(ub5))

        ax6.cla()
        ax6.plot(x, y6, label='range vs time')
        ax6.set_xlabel("Time(s)")
        ax6.set_ylabel('range(m)')
        ax6.set_xbound(next(lb6), next(ub6))

        ax7.cla()
        ax7.plot(x, y7, label='humidity vs time')
        ax7.set_xlabel("Time(s)")
        ax7.set_ylabel('humidity')
        ax7.set_xbound(next(lb7), next(ub7))

        ax8.cla()
        ax8.plot(x, y8, label='momentum vs time')
        ax8.set_xlabel("Time(s)")
        ax8.set_ylabel('momentum')
        ax8.set_xbound(next(lb8), next(ub8))

    plt.tight_layout()


    ani = FuncAnimation(plt.gcf(), animate, interval=2000)

    plt.show()
