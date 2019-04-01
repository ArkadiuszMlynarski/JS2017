import sys

x = 0
lista = []
for i in range(1, len(sys.argv)):
	if(len(sys.argv[i])>=3):
		lista.insert(0, sys.argv[i])
		x=x+1
print(x)
for i in lista:
	print(i, end=" ")