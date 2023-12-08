import random
mylist=[]
v=99
for i in range(0,50):
    # insert into 
    # mylist with values 0 and 1
    v=random.choice([0,1])
    mylist.insert(i,v)
print(mylist)


