#verify the user inputs a valid number
while True:
	num=input('Please enter a number greater or equal to 0\n')
	if num.isdecimal():
		break
num = int(num)

#create a list filled with spaces just the right size in width
positions= [' ' for i in range(num) ]

for j in range(num,0,-1):
	positions[j-1] = '*'
	positions1 = positions
	positions.reverse()
	positions2 = list(positions)
	positions.reverse()
	join_positions1 = ''.join(positions1)
	join_positions2 = ''.join(positions2)
	print(f'{join_positions1}  {join_positions2}')
