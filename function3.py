


def MyListInsert(mydata,myindex,myvalue):
    mydata.insert(myindex,myvalue)
    return mydata


mylist=[12,23,45,56,78,79]
myind=5
myval='shahid'
print(MyListInsert(mylist,myind,myval))

myind=3
myval=[1,2,3,4,5,6,79]
print(MyListInsert(mylist,myind,myval))
