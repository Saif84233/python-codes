with open('sample.txt','r') as file_obj:
	datalist=file_obj.readlines()
	for data in datalist:
		print(data.rstrip())

