import sys
from decimal import Decimal
if len(sys.argv) < 4:
# Skoro instrukcja mówi o liczbach, a nie cyfrach, to warto dokładnie informować użytownika.
# Szczególnie, że skrypt działa dla liczb, nie tylko dla cyfr.
# - MK
	print("Uruchamiajac skrypt podaj pierwsza cyfre, znak oraz druga cyfre")
elif sys.argv[2]=='+':
	print(Decimal(sys.argv[1])+Decimal(sys.argv[3]))
elif sys.argv[2]=='-':
	print(Decimal(sys.argv[1])-Decimal(sys.argv[3]))
elif sys.argv[2]=='*':
	print(Decimal(sys.argv[1])*Decimal(sys.argv[3]))
else:
	print("Potrafie tylko dodawac, odejmowac i mnozyc")