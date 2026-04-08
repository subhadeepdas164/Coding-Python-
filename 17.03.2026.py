# create and print
li=[1,2,3,4,5,]
print(li)

#access element & modify

li[1]=9
print (li)

#add and remove
li.append(7)
print (li)
li.remove(3)
print (li)

#copy using slicing

li1=li[:]
print(li1)

#copy using constructor
newli=list(li)
print(newli)
