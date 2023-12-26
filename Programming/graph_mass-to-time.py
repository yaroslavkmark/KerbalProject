import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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
    X = np.arange(0, 80)
    z = 350000 - 3015.075 * X
    ax.plot(xs, ys, color='r', label='ksp')
    ax.plot(X, z, color='b', label='Мат модель')
    plt.xlabel('Время, с')
    plt.ylabel('Масса, кг')
    plt.title('График массы ко времени полета')
    plt.legend()


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
