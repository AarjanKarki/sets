#creating a set
set1={22,36.8,'hello',False}
print(set1)
set2={10,22,12,14,True,False}
print(set2)
set3={1,1,1,2,2,2,3,5,5,4,4,4}
print(set3)
print(set1|set2)
print(len(set1))
set1.add(200)
print(set1)
set2.remove(True)
for i in set1:
    print(i)
#set operations
set4={1,2,3}
set5={3,4,5}
print(set4|set5)
print(set4.intersection(set5))
print(set4-set5)
print(set4^set5)