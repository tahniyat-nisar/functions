# def sumofdigits(number):
#       sum = 0
#       modulus = 0
#       while number!=0 :
#             modulus = number%10
#             sum+=modulus
#             number/=10
#       return sum
# number=int(input("enter a number:"))
# print(sumofdigits(number))




# def primeorNot(num):
#     if num > 1:
#       count=0
#       for i in range(2,num):
#             if (num % i) == 0:
#                   count+=1
#       if count>2:
#             print(num,"is not a prime number")
#             print(i,"times",num//i,"is",num)            
#       else:
#             print(num,"is a prime number")
# #     else:
#             # print(num,"is not a prime number")
# primeorNot(406)




# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)




# def functionmulti(a,b):
#       multiply=a*b
#       return (multiply)
# print(functionmulti(3,4))



# def Avg(number1,number2,number3):
#       avg=number1+number2+number3/3
#       return(avg)
# print(Avg(1,3,2))



# def voter(age):
#     if age < 18:
#       print("eligible")
#     else:
#       print("not eligible")
#     return(age)
# print(voter(13))


# def distance(kms):
#     if kms < 20:
#       print("close")
#     elif kms < 50:
#       print("median")
#     else:
#       print("far")
#     return(kms)
# print(distance(20))

# def meal(day,time):
#     if day=="sunday":
#       if time=="breakfast":
#             return "dosa"
#       elif time=="lunch":
#             return "dal rice"
#       elif time=="dinner":
#             return "paneer and chapati"
#       else :
#             return "time not found"
#     elif day=="monday":
#       if time=="breakfast":
#             return "fried rice"
#       elif time=="lunch":
#             return "aloo rice"
#       elif time=="dinner":
#             return "chhole bhature"
#       else :
#             return "time not found"
#     elif day=="other":
#       if time=="breakfast":
#             return "aloo"
#       elif time=="lunch":
#             return "rajma rice"
#       elif time=="dinner" :
#             return "veg-chapati"
#       else :
#             return "time not found"

# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))


# def bmi():
#       bmi=weight/height**2
#       if bmi <= 18.5: 
#             return "Underweight"
#       if bmi <= 25.0: 
#             return "Normal"
#       if bmi <= 30.0:
#             return "Overweight"
#       if bmi > 30:
#             return "Obese"
# weight=int(input("enter your body weight:"))
# height=int(input("enter your height:"))
# print(bmi())


# 

# def fun(number):
#       i=1
#       d={}
#       while i<=number:
#             d[i]=i*i
#             i=i+1
#       print(d)
# fun(20)
