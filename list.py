
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

###---List Less Than Ten---###

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = []
#for i in a:
#        if i<10:
#                b.append(i)
#print(b)

#Sum of each number in the list#
#Number = [1,2,3,4,5,6,7,8,9]
#sum = 0
#for each_num in Number:
#    newSum= sum+each_num
#    print(newSum)
#    sum = sum+each_num

#Overlap between 2 Lists#

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []

#for a_num in a:
#    if a_num in b:
#        print(a_num)
