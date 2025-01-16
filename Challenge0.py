#loop for all of the colonne
print('Please enter a number greater or equal to 0')
num = input()
while not num.isdigit() or int(num)<0:
	print('Please enter a number greater or equal to 0')
	num = input()
num = int(num)
for i in range(num+1):
	print('*' * i)