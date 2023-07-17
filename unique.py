l =[]
unique=[]
duplicate=[]
print("enter the 5 numbers")
for i in range(0,5):
    ele=int(input())
    l.append(ele)
print("list=",l)
for i in l:
        if i  not in unique:
            unique.append(i)
        else:
            duplicate.append(i)
print("duplicate",duplicate)
print("unique",unique)
