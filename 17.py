f = open("17.txt")
i = [int(x) for x in f]
c=0
maxqw=0
minqw=0
minbububu=[]
for j in range(len(i)):
    if i[j]>99 and str(i[j])[-1]=="5":
        minbububu.append(i[j])

minqw = min(minbububu)

for d in range(len(i)-1):
    quad=i[d]**2+i[d+1]**2
    if quad%minqw==0:
        if ( len(str(i[d]))==4 and len(str(i[d+1]))!=4 ) or (len(str(i[d+1]))==4 and len(str(i[d]))!=4):
            c+=1
            maxqw=max(maxqw, quad)


print(c,maxqw)
