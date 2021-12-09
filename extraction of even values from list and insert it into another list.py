# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].
def even(List):
    i=0
    k=[]
    while i<len(List):
        if (List[i])%2==0:
            j=List[i]
            k.append(j)
        i+=1
    print(k)
List=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even(List)
