def divisible(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0:
            var_3=i
            sum+=var_3
        elif i%5==0:
            var_5=i
            sum+=var_5
        i+=1
    print(sum)


limit=int(input("enter a number:"))
divisible(limit)