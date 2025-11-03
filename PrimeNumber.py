print('**************************')
print('Chack The Prime Number ')
print('**************************')
print('\n')

def chack ():
    num = int(input("Enter The Number = "))
    count=0
    for i in range(1,num+1):
        if num % i==0:
            count+=1
    if count==2:
        print('This Is Prime Number = ',num)
    else:
        print('This is Not a Prime Number = ',num)
chack()
