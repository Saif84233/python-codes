def add(x,*args):
	sum=x
	for a in args:
		sum=sum+a
	return sum

def info(firstname,lastname,**kargs):
	dict = {'firstname':firstname,'lastname':lastname}
	for k,v in kargs.items():
        	dict[k]=v
	return dict


