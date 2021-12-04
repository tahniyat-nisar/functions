def show_numbers(limit):
    # limit=int(input("enter a number:"))
    i=limit
    while i>0:
        if i%2==0:
            print(i,"is a EVEN")
        else:
            print(i,"is a ODD")
        i-=1
limit=int(input("enter a number:"))
show_numbers(limit)