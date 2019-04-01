import sys
from datetime import date
if len(sys.argv) < 2:
	print("Uruchamiajac skrypt podaj date yyyy-mm-dd")
else:
	date1 = date.today()
	lista = sys.argv[1].split("-")
	date2 = date(int(lista[0]), int(lista[1]), int(lista[2]))
	if date1 > date2:
		date3 = (date1 - date2).days
	else:
		date3 = (date2 - date1).days
	print(date3)