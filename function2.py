
def MyListSum(mylist):
    sum=0
    for i in mylist:
        sum=sum+i
    return sum

def MyListAverage(mylist):
    sum=0
    for i in mylist:
        sum=sum+i
    return sum/len(mylist)
      

mydata=[12,23,45,56,78,79]

a=MyListSum(mydata)
print(a)

avg=MyListAverage(mydata)
print(avg)
