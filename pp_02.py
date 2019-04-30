name = input("Enter Your Name:")
age = input("Enter Your Age:")
try:
    sName= str(name)
    iAge= int(age)
except:
    print("Enter Valid Details")
    quit()
print (sName, iAge)
if iAge>=18:
    print("Your Age is ", iAge, " and You are eligible to Drive")
else:
    print("Your Age is ", iAge, " and You are not eligible to Drive")
