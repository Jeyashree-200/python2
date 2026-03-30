n=input("enter a sentence").split()
d={}
d["store"]="shop"
d["car"]="bike"
d["candy"]="toffy"
d["biscuit"]="cookie"
for i in n:
    if i in d:
        i=d[i]
        print(i,end =" ")
    else:
        print(i,end=" ")
