fname = input('Enter the file name: ')
fhand = open(fname)
counts = dict()
for line in fhand:
    if not line.startswith ("From: "):
        continue
    else:
        splitline= line.rstrip().split()
	for word in splitline:
		if "@" in word:
    		counts[word]= counts.get(word,0)+1
largest = -1
theWord= None
for k,v in counts.items():
    if v>largest:
        largest = v
        theWord = k
print(theWord,largest)
