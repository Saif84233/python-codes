def max(a,b,c):
	if a>=b:
		if a>=c:
			return a
		else:
			return c
	elif b>=c:
		return b
	else:
		return c
maxValue = max(14,10,3)
print(f"maximum is {maxValue}")
