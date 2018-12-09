cena = 100
produkt = 'mleko'
suma = 200

if 100 < suma and suma < 200:
    print('promocja 30%')
    suma = suma - (suma * 30) / 100
elif suma >= 200:
    print('promocj 35%')
    suma = suma - (suma * 35) / 100
else:
    print('bez promocji')

print('do zaplacenia' + str(suma))
