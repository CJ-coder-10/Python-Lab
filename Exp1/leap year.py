year=int(input("Enter a year:"))
if year % 100==0:
    if year % 400==0:
        print(year,"is Leap year")
    else:
        print(year," is not Leap year")
else:
    if year % 4==0:
        print(year,"is Leap year")
    else:
        print(year,"is not Leap year")