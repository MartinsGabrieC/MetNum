#Gabriel Martins de Castro
# 16/0121213

import numpy as np
from matplotlib import pyplot as plt
from math import *

ys = np.array([0.2493938 , 0.72091586, 1.08935177, 0.82557285, 0.15184373,
        -0.55819513, -0.84832015, -1.13075724, -0.66132559, -0.37482053,
        0.49910671, 0.99533713, 0.97493417, 0.56770796,-0.59740919,
        -0.76333201, -1.05362856, -0.8085086 , -0.32029816, 0.4021104])

ts = np.array([0., 5.26315789, 10.52631579, 15.78947368,
        21.05263158, 26.31578947, 31.57894737, 36.84210526,
        42.10526316, 47.36842105, 52.63157895, 57.89473684,
        63.15789474, 68.42105263, 73.68421053, 78.94736842,
        84.21052632, 89.47368421, 94.73684211, 100.])

#função e suas derivadas
def EQ(w):
    EQ = 0
    for i in range(20):
        EQ += (sin(w*ts[i]) - ys[i])**2
    return EQ

#gráfico de EQ
listay = []
listax = []
for w in range(20):
    wo = w/100
    listay.append(EQ(wo))
    listax.append(wo)
# plt.plot(listax,listay)
# plt.show()

#mínimo de função
x1= 0
x2= 0.2

for i in range(10):
    xa = x1 + (x2 - x1)/3.0
    xb = x1 + (x2-x1)*2/3.0

    EQa = EQ(xa)
    EQb = EQ(xb)

    if EQa > EQb:
        x1 = xa
    else:
        x2 = xb

    if EQa < EQb:
        print(xa)
    else:
        print(xb)

#O resultado mostra que o mínimo está em 0.13
