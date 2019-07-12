fname = input("Enter file name: ")
fh = open(fname)
result = 0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #Float = float(line [20:30].rstrip())
    Float = float(line.split().rstrip())
    #print (Float)
    result = result + Float
    count = count+1
print ("Average spam confidence:", result/count)

#Shines like a moon, sparkles like a star, glows like a sun
#My little doll became one year old with so much fun
#Time flies like flash of lights with mesmerizing moments
#Engraves in my soul for life, that I cannot even comment
#Beautiful smile with sparkling eyes
#Makes me fly on the clouds in the skies
#I am so lucky and Blessed to have you my daughter
#Stands strong and holds you always as I am your Father
