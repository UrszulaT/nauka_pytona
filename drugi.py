marka = 'Peugeot'
ilosc_drzwi = 5
pojemnosc = 1.3
marka_up = marka.upper()

print("Samochod " + marka + " ma " + str(ilosc_drzwi) + " drzwi")
print(marka_up)
print("Pojemnosc po zmianach: " + str(pojemnosc * 2))
if ilosc_drzwi > 3:
    print('Duzy samochod')
else:
    print('Maly')

if marka == 'Peugeot':
    print('Francuski samochod!')
else:
    print('Inny')
  
