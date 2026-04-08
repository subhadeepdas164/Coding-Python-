a=0
b=1
n=int (input("enter the reng n"))
print(a)
print(b)
for i in range (n-2):
    next =(a+b)
    print (next)
    a=b
    b=next
