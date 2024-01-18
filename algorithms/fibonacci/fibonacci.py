def fibonacci(n: int) -> int:
	if n == 0:
		return 0
	elif (n <= 2):
		return 1
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

num = 11

if num <= 0:
	print("Enter a positive integer")
else:
	for i in range(num):
		print('fibonacci('+str(i)+') = ' + str(fibonacci(i)))
