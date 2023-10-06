#Sandrah Lewa 
#SCT211-0090/2022

Year = int(input("Enter year:"))
if (Year%400 == 0) and (Year%100 == 0) :
    print ("Year entered is a leap year ")
elif (Year%4 == 0) and (Year%100 != 0) :
    print ("Year entered is a leap year")
else:
    print("Year entered is not a leap year")