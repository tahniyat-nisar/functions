# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
def elements_sum():
    i=0
    c=[]
    while i<len(List):
        a=List[i]
        rev1=a%10
        rev2=a//10
        sum=rev1+rev2
        c.append(sum)
        i+=1
    return(c)
List=[12, 67, 98, 34]
print(elements_sum())
