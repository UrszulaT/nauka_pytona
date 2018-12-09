kawa = [ 'espresso' , 'cappuccino' , 'caffe latte' , 'flat white' , 'americano']

print(kawa[2])
print(kawa[4])

for s in kawa:
    print(s)

for idx in range( len(kawa)):
    print("idx: " + " : " + kawa[idx])

print(",".join(kawa))

arr = "a,b,c,d,e" .split(',')
print (arr)

for idx in range ( len(kawa) ):
    print("idx: " + str(idx) + ":" + kawa[idx])
