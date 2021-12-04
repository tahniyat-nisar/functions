
# def perfect():
#     num=range(1,1001)
#     for x in num:
#         original=x
#         i=1
#         sum=0
#         while i<x:
#             if x%i==0:
#                 sum=sum+i 
#             i+=1
#         if sum==original:
#             print(original,"is a perfect number")
#         else:
#             print(original,"is not a perfect number")

# perfect()



def perfect():
    num=1
    while num<=1000:
        original=num
        i=1
        sum=0
        while i<num:
            if num%i==0:
                sum=sum+i 
            i+=1
        if sum==original:
            print(original,"is a perfect number")
        else:
            print(original,"is not a perfect number")
        num+=1

perfect()