fruit = "banana"
index = 0
length = len(fruit)
while index <len(fruit):
    letter = fruit[index]
    print (index, letter)
    index = index+1

fName='Mithilesh'
lName='Satapathy'
indexfName= 0
indexlName=0
print(len(fName), len(lName), fName, lName)
while indexfName<9 and indexlName<9:
    letterfName = fName[indexfName]
    letterlName = lName[indexlName]
    print(indexfName,letterfName,letterlName)
    indexfName = indexfName+1
    indexlName = indexlName+1

iName = 'mithilesh'
sName = 'satapathy'
for letter in (iName):
    print(letter)
for letter in (sName):
    print(letter)
