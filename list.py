
###1.0---- This is a nested list to Print---###

##Numbers = [1,2,3,[4,5,6,[7,8,9]]]
##
##for each_num in Numbers:
##        if isinstance (each_num,list):
##                for sub_num in each_num:
##                        if isinstance (sub_num,list):
##                                for nest_num in sub_num:
##                                        print (nest_num)
##                        else:
##                                print (sub_num)
##        else:
##                print(each_num)
##
##

###2.0--- This is to print odd and even number ---###
##array = [23,45,67,89,56,46,37,78]
##for each_num in array:
##        if each_num % 2 ==0:
##                print("This is an even number")
##        else:
##                print ("This is an odd number")

###3.0--- Print name and age as user input ---###

##Name = input("Enter your Name:")
##print ("Your Name is : " + Name)
##Age= int(input("Enter your Age:"))
##print("Your Age is: " + str(Age))
##turn100Years= str(2020-Age+100)
##print("You will turn 100 Years old in the Year :" + str(turn100Years))

###4.0---List Less Than Ten---###

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = []
#for i in a:
#        if i<10:
#                b.append(i)
#print(b)

#5.0Sum of each number in the list#
#Number = [1,2,3,4,5,6,7,8,9]
#sum = 0
#for each_num in Number:
#    newSum= sum+each_num
#    print(newSum)
#    sum = sum+each_num

#6.0Overlap between 2 Lists#

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []

#for a_num in a:
#    if a_num in b:
#        print(a_num)

###7.0 Print the name to see if it is Palindrom
#name= input("Enter your Name:")
#rvsName= name[::-1]
#if name==rvsName:
#    print("This is Palindrome")
#else:
#    print("This is not Palindrome")

###8.0 Print the new list with only even numbers from another list
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#b = []
#for number in a:
#    if number %2==0:
#        b.append(number)
#print(b)
###
##import turtle
##
##screen = turtle.Screen()
##screen.bgcolor("white")
##screen.title("Drawing Birthday Wish")
##
##my_turtle = turtle.Turtle()
##my_turtle.pensize(5)
##my_turtle.shape("circle")
####my_turtle.forward(100)
##
####for move in range(0,1):
##my_turtle.forward(20)
##my_turtle.right(90)
##my_turtle.forward(50)
##my_turtle.backward(100)
##my_turtle.forward(50)
##my_turtle.right(90)
##my_turtle.forward(40)
##my_turtle.right(90)
##my_turtle.forward(50)
##my_turtle.backward(100)
##
##my_turtle.penup(100)
####my_turtle.backward(50)
##    
##
##my_turtle.hideturtle()
##turtle.done()

##def factorial(n):
##    if not isinstance (n,int):
##        return -1
##        print("Factorial is not Integers")
##    elif n<0:
##        return -1
##        print("Factorial is only for Positive Numbers")
##    elif n == 0:
##        return 1
##    else:
##        return n*factorial(n-1)
##print (factorial(1024))
##
##def isdivisible (x,y):
##    if x%y ==0:
##        return ("This is an Even Number")
##    else:
##        return ("This is an odd Number")
##
##print (isdivisible(98659465943659935654359456423965546954876956754967546095762672760297,7696769726969762946759649237659432567596))
####### BReak Statement #########
##num = [1,2,3,4,5,6,7]
##for i in num:
##    if i ==5:
##        break
##    else:
##        print(i)
##    
##count = 0
##i = 0
##while i >=0:
##    if count == 100:
##        break
##    else:
##        print(i, count)
##    count = count +1


