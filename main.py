import matplotlib.pyplot as plt
from decimal import Decimal
from sympy import *
x = Symbol('x', real=True)


class Mirroring:

    def __init__(self, f_x, g_x, min_v, max_v, step):
        self.f_x = f_x
        self.g_x = g_x
        self.z_x = [[],[]]
        self.min_v = min_v
        self.max_v = max_v
        self.step = step

    def points_calculation(self, x0, y0):
        length = (x - x0) ** 2 + (g_x - y0) ** 2
        diff_length = diff(length)
        roots = solve(diff_length)
        d_extremes = []

        if len(roots) > 0:
            for i in range(len(roots)):
                gfg = roots[i].as_real_imag()
                roots[i] = gfg[0].evalf()
                d_extremes.append(length.subs(x, roots[i]).evalf())

            graph_x = roots[d_extremes.index(min(d_extremes))]
            graph_y = self.g_x.subs(x, graph_x)

            x1 = sympify(float(2 * graph_x - x0))
            y1 = sympify(float(2 * graph_y - y0))

            return x1, y1

    def plot_calculation(self):
        i = Decimal(str(self.min_v))  # минимальное знаение x для отражаемой функции
        while i <= self.max_v:  # максимальное знаение x для отражаемой функции
            print(str((i-self.min_v)/(self.max_v-self.min_v)*100)+'%')
            x1 = float(i)
            y1 = f_x.subs(x, x1)
            c = self.points_calculation(x1, y1)

            if c != None:
                self.z_x[0].append(c[0])
                self.z_x[1].append(c[1])
            i += Decimal(str(self.step))  # шаг значений x

    def plot_draw(self, f_x):
        new_points = [[], []]
        i = Decimal(str(self.min_v))  # минимальное знаение x для функции относительно которой идет отражение
        while i <= self.max_v:  # максимальное знаение x для функции относительно которой идет отражение
            new_points[0].append(i)
            new_points[1].append(f_x.subs(x, i))
            i += Decimal(str(self.step))  # шаг значений x
        return new_points


    def run(self):
        self.plot_calculation()
        f_x_draw = [self.plot_draw(f_x,)[0], self.plot_draw(f_x)[1]]
        g_x_draw = [self.plot_draw(g_x)[0], self.plot_draw(g_x)[1]]

        plt.plot(self.z_x[0], self.z_x[1], f_x_draw[0], f_x_draw[1], g_x_draw[0], g_x_draw[1])
        plt.axis([-10, 10, -10, 10])
        plt.grid(True)
        plt.show()


f_x = x-2     #отражаемая функция
g_x = x**2+2*x+1  #функция относительно которой отражают

Solution = Mirroring(f_x, g_x, -10, 10, 0.2)
Solution.run()
