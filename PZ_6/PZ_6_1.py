title = []

try:
	n = int(input("Input N size: "))
	k = int(input("Input K: "))
	l = int(input("Input L: "))
except:
	print('You must be input integer numbers, not other!')
	exit()

if 1 < k <= l <= n:
	result = 0

	for i in range(n):
		title.append(i)

	title = title[:k] + title[l:]

	for i in title:
		result += i

	average = result / len(title)
	print('Average: ', average)
else:
	print('Please read a task and retry later')

