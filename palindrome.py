#Palindrome Number 
print("****************************")
print(" Chack Palindrome Number ")
print("****************************")
print("\n")
num = int(input('Enter The Number '))
number=num
rev=0

while(number>0):
    rev = rev*10 + number%10
    number  =  number//10


if rev==num:
    print('This is Pelindrome Number = ', num)

else :
    print('Not Palindrome')    