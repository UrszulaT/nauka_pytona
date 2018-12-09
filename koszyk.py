koszyk = [
    {'name' : 'mleko', 'cena' : 10},
    {'name' : 'ser', 'cena' : 4.0},
    {'name' : 'pomidory', 'cena' : 5.25},
    {'name' : 'oliwa' , 'cena' : 15}
]
print(koszyk[0] ['cena'])

suma = 0
for poz in koszyk:
    suma = suma + poz['cena']
print(suma)

# mleko i ser => 10%
#stan_reguly = {'mleko' : False, 'ser': False}
bylo_mleko = False
byl_ser = False

suma = 0

for poz in koszyk:
    suma = suma + poz['cena']
    nazwa_prod = poz['name']
    if nazwa_prod == 'mleko':
        bylo_mleko = True
    if nazwa_prod == 'ser':
        byl_ser = True

if bylo_mleko and byl_ser:
    suma = suma - (suma * 10) / 100
print(suma)
