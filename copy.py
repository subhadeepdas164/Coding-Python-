a = [1, 2, 3]
b = a
c=a.copy()
b.append(7)
c.append(4)



print(a)  
print(b)
print (c)


# to make a and b diff

import  copy
a=[[1,2],[3,4]]

b=copy.deepcopy(a)
b[0].append(10)
print(a)
print(b)
