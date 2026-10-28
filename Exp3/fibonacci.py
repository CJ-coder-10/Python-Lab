num1,num2=0,1
num=int(input("Enter a number:"))
print(" ",num1)
print(" ",num2)
for i in range(2,num+1):
    num3=num1+num2
    print(" ",num3)
    num1=num2
    num2=num3
