f = open('a1.txt', 'r')


a = [i for i in range(10)]

print a

for line in f:
	su = 0;
	for el in line.split(", "):
		try:
			su = su + int(el)
		except:
			pass
	print su


# int, float,
# functions
# lambda
# try catch
# xml parser

# numpy
# Matplotlib
# pandas