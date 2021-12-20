print(
'''
Enter Matrix as a Nested List for Example a 3 x 3 Matrix such as  :
[1 2 3]
[0 9 1]
[8 2 3]
will be enterd as :
[[1,2,3],[0,9,1],[8,2,3]]
''')
Matrix1=eval(input("Enter the First Matrix : "))
Matrix2=eval(input("Enter the Second Matrix : "))
result = []
for i in range(len(Matrix1)):
        result_row=[]
        for j in range(len(Matrix2[0])):
                sum=0
                for k in range(len(Matrix2)):
                        sum+=Matrix1[i][k] * Matrix2[k][j]
                result_row.append(sum)
        result.append(result_row)
for row in result:
    print(row)
