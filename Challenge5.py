import math
#verify the user inputs a valid number
print('Please enter a whole number greater or equal to 0')
num = input()
while not num.isdigit() or int(num)<0:
	print('Please enter a number greater or equal to 0')
	num = input()
num = int(num)
#if the user feels lazy, respond!
if num == 0 or num == 1:
	print('*' * num)
	print('Seriously...I worked hard on this you know.')
	exit()
#create a list filled with spaces just the right size in width
positions= []
for j in range (0, (2 * num) - 1, 1):
	positions.insert(0,' ')
#replace all the slots in the middle, and growing outward with *
for i in range (len(positions)):
	try:
		positions[(math.floor (len(positions) / 2)) + i] = '*'
		positions[(math.floor (len(positions) / 2)) - i] = '*'
		print(''.join(positions))
	except IndexError:
		break
