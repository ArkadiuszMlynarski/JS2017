import sys
from math import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
delta = b*b-4*a*c

if(delta>0):
	print(2)
# 'deltaa' to nie jest zbyt fortunna nazwa, gdyby ten kod miał
# kilkaset linii, to po jakimś czasie pewnie wyciągnąłby Pan pierwiastek 
# z 'deltaa' jeszcze raz i bug gotowy. Albo zrobiłby to ktoś inny, kto kod by przejął.
# Może lepiej delta_sqrt, deltasqrt, sqrt_of_delta?
# - MK
	deltaa = sqrt(delta)
	x1=(-b+deltaa)/(2*a)
	x2=(-b-deltaa)/(2*a)
	print(x1, x2)
	
if(delta==0):
	print(1)
	deltaa = sqrt(delta)
	x1=(-b)/(2*a)
	print(x1)
	
if(delta<0):
	print(0)