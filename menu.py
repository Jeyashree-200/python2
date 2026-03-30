r1=int(input("Rows of A:"))
c1=int(input("Columns of A:"))
r2=int(input("Rows of B:"))
c2=int(input("Columns of B:"))
if c1!=r2:
    print("Multiplication not possible")
else:
    print("Matrix A:")
    A=[list(map(int,input().split())) for i in range(r1)]
    print("Matrix B:")
    B=[list(map(int,input().split())) for i in range(r2)]
    result=[]
    for i in range(r1):
        rows=[]
        for j in range(c1):
            rows.append(0)
        result.append(rows)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]+=A[i][k]*B[k][j]
    print("Result Matrix:")
    for row in result:
        print(row)
