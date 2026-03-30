students=[]
n=int(input("enter no of sudent:"))
for i in range(n):
    s_id=int(input("enter student id:"))
    name=(input("enter name:"))
    marks=int(input("enter marks:"))
    student=(s_id,name,marks)
    students.append(student)
students=tuple(students)
print("\n\tstudent details:")
for s in students:
    print("ID:",s[0],"name:",s[1],"marks:",s[2])
key=int(input("enter student id:"))
f=0
for s in students:
    if s[0]==key:
        print("ID:",s[0],"name:",s[1],"marks:",s[2])
        f=1
if not f:
        print("student not found")
max=students[0]
for s in students:
    if s[2]>max[2]:
        max=s
        print("ID:",s[0],"name:",s[1],"marks:",s[2])
t=0
for s in students:
    t=t+s[2]
avg=t/len(students)
print("\naverage marks:%2f",avg)
