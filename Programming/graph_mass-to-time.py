import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    data = open('mass-time.txt', 'r').read()
    lines = data.split('\n')

    xs = []
    ys = []

    for line in lines:
        try:
            x, y = line.split(', ')
            xs.append(float(x))
            ys.append(float(y))
            
        except:
            pass

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel('t')
    plt.ylabel('m')
    plt.title('График массы ко времени полета')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
