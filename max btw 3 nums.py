def maximum():
    count=1
    max=0
    while count<=3:
        n=int(input("enter a number:"))
        if n>max:
            max=n
        count+=1
    print(max)
(maximum())
