fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    stripline = line.rstrip()
    lines = stripline.split(" ")
    for word in lines:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
