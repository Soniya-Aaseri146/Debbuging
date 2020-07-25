list=[7,10,7,2,3,-21,1,6]
i=0
while i<len(list):
  	j=0
    while j<len(list):
		if list[i]<list[j]:
			a=list[i]
			list[i]=list[j]
			list[j]=a
		j=j+1
	i=i+1
print list
		
count=[]
def adjacentElementsProduct(inputArray):
    i=0
    sum=0
    j=i+1
    while j<len(inputArray):
        sum=inputArray[i]*inputArray[j]
        count.append(sum)
        i=i+1
        j=j+1
    b=0
    largest=count[b]
    while b<len(count):
        if count[b]>largest:
            largest=count[b]
        b=b+1
    return largest
print adjacentElementsProduct([-1,4,6,7,-17])