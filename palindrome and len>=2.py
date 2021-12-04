# Q1.Write a Python program to count the number of strings where the string length is 2
# the first and last characters are the same from a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221']
# result= 2


def length_str(l):
    i=0
    count=0
    while i<len(l):
        a=l[i]
        if a[-1]==a[0] and len(a)>=2:
            count+=1
        i+=1
    return (count)
l=['abc', 'xyz', 'aba', '1221']
print(length_str(l))


def length_str(l):
    count=0
    for i in l:
        if len(i)>=2 and i[-1]==i[0]:
            count+=1
    return (count)
l=['abc', 'xyz', 'aba', '1221']   
print(length_str(l))
