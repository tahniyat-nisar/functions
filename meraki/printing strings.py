def string(name1,name2):
    if len(name1)==len(name2):
        print(name1)
        print(name2)
    elif len(name1)>len(name2):
        print(name1)
    elif len(name1)<len(name2):
        print(name2)

name1=input('enter a name:')
name2=input('enter a name:')
string(name1,name2)