print("************************")
print("Chack The Neon Number ")
print("************************ \n")

def neon ():
    num = int(input('Enter The Number = '))
    ans = pow(num,2)
    number = 0
    while ans>0:
        number = number + ans%10
        ans=ans//10
    if number==num:
        print('This Is Neon Number = ',num)    
    else:
        print('This Is Normal Number = ',num)
neon()        