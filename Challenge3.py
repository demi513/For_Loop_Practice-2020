print('Please enter a number greater or equal to 0')
num = input()
while not num.isdigit() or int(num)<0:
	print('Please enter a number greater or equal to 0')
	num = input()
num = int(num)
for i in range(1, num+1):
	print( str(str(i) * i) + str('*' * (num - i)))