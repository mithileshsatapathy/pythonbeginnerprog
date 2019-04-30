fruit = 'banana'
count = 0
for letter in fruit:
    if letter == 'a':
        count = count+1
        print(count)
pos = fruit.find('an')
print (pos)
print(fruit.upper())
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
x = '40'
y = int(x) + 2
print(y)
x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])
print(len('banana')*7)
greet = 'Hello Bob'
print (greet.upper())
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475";
colFind = text.find('0')
numFind = text.find('5',colFind)
print(colFind)
print(numFind)
result = text [colFind : numFind+1]
print (float(result))
