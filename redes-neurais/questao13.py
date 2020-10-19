def output(d):
	if d >= 0:
		return 1
	return -1

def individual_error(o, f):
	return o - f

def sum(w, x):
	d = w[0]
	for i in range(2):
		d += w[i+1]*x[i]
	return d

def summation(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

def global_error(e):
    return 0.5*summation(e) ** 2

x1 = [1,0,4,5,1,6]
x2 = [1,2,3,4,0,4]
table_class = [1, 1, -1, -1, 1, -1]
weight = [1, 1, 1]
rate = 0.01
error, delta1, delta2 = [], [], []
aux = -1

while aux < 0:
	error.clear()
	delta1.clear()
	delta2.clear()

	print('| x1 | x2 |  d    | f |  o  | Atual | Alvo  | e  | delta1 | delta2 |')

	for i in range(len(x1)):
		x = [x1[i], x2[i]]
		d = sum(weight, x)
		f = output(sum(weight, x))
		actual = 'A' if f > 0 else 'B'
		target = 'A' if table_class[i] > 0 else 'B'
		error.append(individual_error(table_class[i], f))
		delta1.append((rate * error[i] * x1[i]))
		delta2.append((rate * error[i] * x2[i]))
		line = [x1[i], x2[i], d, f, table_class[i], actual, target, error[i], delta1[i], delta2[i]]
		print('| {:}  | {:}  |  {:.2f} | {:} | {:>2}  |   {:}   |   {:}   | {:>2} |   {:>2,.2f}  |  {:>2,.2f}  |'.format(*line))

	print('Peso: {}'.format(weight))
	print('Erro Global: {}'.format(global_error(error)))
	print('Erro Global elevado a 2: {}\n'.format(global_error(error) ** 2))

	if (global_error(error) ** 2) != 0:
		weight[1] = weight[1] + summation(delta1)
		weight[2] = weight[2] + summation(delta2)
	else:
		aux = 1