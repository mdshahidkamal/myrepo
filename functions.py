mylist=[16,15,10,19,15,16,12,11,16,10,0,1,1,1,1,1,0,0,0,0]

def GetOddEven():
    for num in mylist:
        if num%2==0:
            print(str(num)+ ' is even')
        else:
            print(str(num)+ ' is odd')

def Sum():
    result=0
    for num in mylist:
        result=result+num
        print(result) #sum

def Average():
    result=0
    for num in mylist:
        result=result+num
    print(result/len(mylist))#average
