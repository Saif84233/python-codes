def sum(x,y):
	return x+y
def sumArray(x):
	s=0
	for data in x:
		s=s+data
	return s
salaries =[200,500,750,280,320]
result= sumArray(salaries)
print(f"sum of salaries is {result}")

