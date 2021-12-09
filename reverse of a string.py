Sample String : "1234abcd"
Output : "dcba4321".
def reverse(string):
    i=1
    sum=""
    while i<=len(string):
        x=string[-i]
        sum=sum+x
        i+=1
    return(sum)
print(reverse("1234abcd"))
