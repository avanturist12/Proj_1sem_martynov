def mean(x, y):
	if x > 0 and y > 0:
		a_mean = float((x + y) / 2)
		g_mean = float(y / x * y)

		return a_mean, g_mean
	else:
		return "You must use only positive numbers to get the result"


try:
	a = int(input("Input a: "))
	b = int(input("Input b: "))
	c = int(input("Input c: "))
	d = int(input("Input d: "))

	print(mean(a, b))
	print(mean(a, c))
	print(mean(a, d))
except:
	print('You must be input integer numbers!')

