# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20.

def list_sum():
    i=0
    sum=0
    while i<len(l):
        sum=sum+l[i]
        i+=1
    return(sum)
l=[8, 2, 3, 0, 7]
print(list_sum())



def list_sum():
    sum=0
    for i in l:
        sum=sum+i
    return(sum)
l=[8, 2, 3, 0, 7]
print(list_sum())
