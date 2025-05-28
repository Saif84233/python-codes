skills = {'kaif':['python'],'saif':['c','python'],'aurijeet':['c','java','bash']}
for key,value in skills.items():
	print(f"student name: {key}")
	for  language in value:
		print(f"\t language:{language}")
