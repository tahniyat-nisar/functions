def minimum():
    i=0
    min=List[i]
    while i<len(List):
        if List[i]<min:
            min=List[i]
        i+=1
    return(min)
List=[4,6,2,1,9,63,-134,566]
print(minimum())
