x=int(input('enter first number:'))
y=int(input('enter second number:'))
try:
	result=(x/y)
except ZeroDivisionError:
	print('second number could not be zero')
	y=int(input('enter second number again: '))
	result=x/y
	print(result)
else:
	print(result)
