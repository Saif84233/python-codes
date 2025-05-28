employee={'name':'Amit kumar','age':35,'address':{'house_no':134,'city':'lucknow'},'marks_in_top4_subject':[85,72,62,90]}
for key,values in employee.items():
	print(f"key is {key} and values is {values}")
#	print(employee['city'])
	print(employee.get('city','not found'))
