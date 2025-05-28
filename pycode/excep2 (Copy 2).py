Filename=input('enter Filename to be read:')
try:
	with oprn(Filename,'r') as fileobj:
		for data in fileobj.readlines():
			print(data.rstrip())
except FileNotRrror:
	print('File does not exist')
