max = None
min = None
while True:
    number = input("Enter your Number:")
    if number == "done":
        break
    try:
        num = int(number)
    except:
        print("Invalid input")
        continue
    if num > max:
        max = num
        continue
    if num < max:
       	min = num
    continue
print("Maximum is", max)
print("Minimum is", min)

7,2,bob,10,4
