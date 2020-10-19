from util import output, individual_error, sum, summation, global_error
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms

x1 = [8, 1, 4, 2]
x2 = [3, 1, 2, 1]
table_class = [1, -1, -1, 1]
weight = [-1, 0.45, 0.10]

print('--- LETRA A) ---')
print('| x1 | x2 |  d      |')
for i in range(len(x1)):
    x = [x1[i], x2[i]]
    d = sum(weight, x)
    line = [x1[i],  x2[i],  d]
    print('| {:}  | {:}  |  {:.2f}  |'.format(*line))


print('\n--- LETRA B) ---')
print('| x1 | x2 |  d      | f |  o  |')
for i in range(len(x1)):
    x = [x1[i], x2[i]]
    d = sum(weight, x)
    f = output(sum(weight, x))
    line = [x1[i],  x2[i],  d, f, table_class[i]]
    print('| {:}  | {:}  |  {:.2f}  | {:} | {:>2}  |'.format(*line))

print('\n--- LETRA C) ---')
print('| x1 | x2 |  d      | f |  o  | Atual |')
for i in range(len(x1)):
    x = [x1[i], x2[i]]
    d = sum(weight, x)
    f = output(sum(weight, x))
    actual = 'A' if f > 0 else 'B'
    line = [x1[i],  x2[i],  d, f, table_class[i], actual]
    print('| {:}  | {:}  |  {:.2f}  | {:>2} | {:>2}  |  {:}   |'.format(*line))

print('\n--- LETRA D) ---')
error = []
print('| x1 | x2 |  d      | f |  o  | Atual || e  |')
for i in range(len(x1)):
    x = [x1[i], x2[i]]
    d = sum(weight, x)
    f = output(sum(weight, x))
    actual = 'A' if f > 0 else 'B'
    error.append(individual_error(table_class[i], f))
    line = [x1[i],  x2[i],  d, f, table_class[i], actual, error[i]**2]
    print('| {:}  | {:}  |  {:.2f}  | {:>2} | {:>2}  |  {:}   | {:>2}  |'.format(*line))
print('Erro Global: {}'.format(global_error(error)))
print('Erro Global elevado a 2: {}'.format(global_error(error) ** 2))

print('\n--- LETRA F) ---')
error, delta1, delta2 = [], [], []
rate = 0.02
weight = [-1, 0.45, 0.10]
print('| x1 | x2 |  d      | f |  o  | Atual | e  | delta1 | delta2 |')
for i in range(len(x1)):
    x = [x1[i], x2[i]]
    d = sum(weight, x)
    f = output(sum(weight, x))
    actual = 'A' if f > 0 else 'B'
    error.append(individual_error(table_class[i], f))
    delta1.append((rate * error[i] * x1[i]))
    delta2.append((rate * error[i] * x2[i]))
    line = [x1[i],  x2[i],  d, f, table_class[i], actual, error[i]**2, delta1[i], delta2[i]]
    print('| {:}  | {:}  |  {:.2f}  | {:>2} | {:>2}  |  {:}   | {:>2}  |   {:>2,.2f}  |  {:>2,.2f}  |'.format(*line))
print('Erro Global: {}'.format(global_error(error)))
print('Erro Global elevado a 2:'.format(global_error(error) ** 2))
weight[1] = weight[1] + summation(delta1)
weight[2] = weight[2] + summation(delta2)
print('w0: {} | w1: {} | w2: {}'.format(weight[0], weight[1], weight[2]))

print('\n--- LETRA E) ---')
fig, ax = plt.subplots()
ax.scatter(x1, x2, c = 'red')
line = mlines.Line2D([0, 1], [0, 1], color='green')
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)
plt.show()