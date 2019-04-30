score = input("Enter Score: ")
try:
    fScore= float(score)
except:
    print("Enter Valid Score between 0.0 to 1.0")
    quit()
if fScore>1.0:
    print("Your Score is out of Range")
if fScore >=0.9 and fScore<=1.0:
    print("A")
elif fScore>=0.8 and fScore<0.9:
    print("B")
elif fScore>=0.7 and fScore<0.8:
    print("C")
elif fScore>=0.6 and fScore<0.7:
    print("D")
elif fScore<0.6:
    print("F")
#else:
#    ("Your Score is out of Range")
