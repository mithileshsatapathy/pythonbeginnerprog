largest = 0
smallest = 0
while True:
    number = input ("Enter a Number:")
    try:
        num = int (number)
    except:
        print("Invalid input")
    if number > largest:
        largest == number
        print("Maximum is :", number)
        continue
    if number < largest:
        smallest==number
        print("Maximum is :", number)
        print("Minimum is :", number)
        continue
    if number == "done":
        quit()
