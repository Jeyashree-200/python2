d={}
n=int(input("enetr no of student:"))
for i in range(n):
    name=input("enter student name:")
    marks=int(input("enter marks:"))
    d[name]=marks
print(d)
key=input("enter student name:")
if key in d:
    print("the mark of ",key,"is",d[key])
else:
    print("student not found")
