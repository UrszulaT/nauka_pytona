koszyk = ['mleko', 'woda','oliwa', 'sok']
cena = [20, 40, 60, 90]

suma = 0

for c in cena:
    suma = suma + c

print(suma)

if suma >= 500 :
    print("znizka 20%, >500pln")
    suma = suma - (suma * 20.0)/100
elif len(koszyk) > 3 :
    print("znizka 15%")
    suma = suma - (suma * 15.0) / 100
else:
    print("bez promocji")

print("do zaplacenia:{0}".format(suma))
