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