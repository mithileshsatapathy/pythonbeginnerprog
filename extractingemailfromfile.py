fname = input("Enter file name: ")
fh = open(fname)
lst = []
count = 0
for line in fh:
    if not line.startswith ("From "):
        continue
    else:
        stripline = line.rstrip().split()
    print(stripline[1])
    count = count+1
print("There were", count, "lines in the file with From as the first word")
