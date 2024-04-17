def findTotalOccurence(listOfNumbers,target):
    result=0
    n=len(listOfNumbers)
    for index in range(n):
        if listOfNumbers[index]==target:
            result=result+1
    return result

listOfNumbers=[12,34,21,12,34,55,34,12]
target=34

result=findTotalOccurence(listOfNumbers,target)

print("total number of occurences:",result)
list2=[12,33,54,56,4,3,2,1,23,45,23]
target2=23
result2=findTotalOccurence(list2,target2)
print(result2)
