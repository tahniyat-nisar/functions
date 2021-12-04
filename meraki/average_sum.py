def average():
    n=int(input("enter the count of how many numbers average you want:"))
    count=0
    sum=0
    while count<n:
        a=int(input("enter a number:"))
        sum=sum+a
        count+=1
    return(sum//count)

print(average())






