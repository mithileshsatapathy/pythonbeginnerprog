# Print the numbers 1-20
num = (34,45,56,32,99,3,6,9,0)
before=-1
for i in num:
    if i>before:
        before =i
        print(i)
        i=i+1
