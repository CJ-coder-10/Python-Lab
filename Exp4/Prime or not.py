flag=1
num=int(input("Enter a number:"))
if num==1:
    print(num,"is neither prime nor composite!")
else:
    for i in range(2,int(num/2)+1):
        if num % i ==0:
            flag=0
            break
    if flag==1:
        print(num,"is a prime number!")
    else:
        print(num,"is a composite number!")