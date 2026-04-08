tup=('A','B','C','D','A','B','C','D')
print("original tuple:", tup)
li=list(tup)
li[0]="hello"
li[1]="world"
li[2]="python"
print("modified list:", li)



a=(3,4,5)
b=[3,4,5]
b[0]=10
print(b)
c=list(a)
c[0]=12
a=tuple(c)
print(a)




a=[1,5,8,14,20,25,35,40,50,60]
print (a[0:])
print(a[1:9:2])
print (a[-1])





a=[1,5,8,14,20,25,35,40,50,60]
print (a[9::-1])



a=[1,5,8,14,20,25,35,40,50,60]
print("Reverse printing",a[9::-1])
print ("Reverse printing ",a[-5:0:-2])


a=[1,5,8,14,20,25,35,40,50,60]
print("Reverse printing",a[::-1])
str = "Sayandip khatua"
str[0]="S"
print (str)


a=[1,5,8,14,20,25,35,40,50,60]
print("Reverse printing",a[::-1])
str= "Sayandip khatua"
print (str == str[::-1])
