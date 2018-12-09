samochody = ('syrena' , 'polonez', 'opel' , 'kia')
print(samochody[0])
print(samochody[2])
for s in samochody:
    print(s)

for idx in range( len(samochody)) :
    print("idx: " + str(idx) + " : " + samochody[idx])
