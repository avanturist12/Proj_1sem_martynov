def mean(x, y):
	if x > 0 and y > 0:
		a_mean = float((x + y) / 2)
		g_mean = float(y / x * y)

		return a_mean, g_mean
	else:
		return "введите числа!"


try:
	a = int(input("Input a: "))
	b = int(input("Input b: "))
	c = int(input("Input c: "))
	d = int(input("Input d: "))

	print(mean(a, b))
	print(mean(a, c))
	print(mean(a, d))
except:
	print('Вы ввели правельные числа!')

