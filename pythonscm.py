### print("------------------------------------------------------------------")
print("|                 1} ADDITION                                    |")
print("|                 2} SUBTRACTION                                 |")
print("|                 3} MULTIPLICATION                              |")
print("|                 4} FIND DETERMINANT                            |")
print("|                 5} SYMMETRIC                                   |")
print("|                 6} SKEWSYMMETRIC                               |")
print("------------------------------------------------------------------")
print("give input correctly")


def Addition():
    m = int(input("Enter number of rows : "))
    n = int(input("Enter number of columns : "))

    matrix1 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix1 :")))
        matrix1.append(x)
    matrix2 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix2 :")))
        matrix2.append(x)
    print("matrix1: ")
    for i in matrix1:
        print(i)
    print("matrix2: ")
    for i in matrix2:
        print(i)

    Total = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(0)
        Total.append(x)

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            Total[i][j] = matrix1[i][j] + matrix2[i][j]

    print("Addition of both the matrices: ")
    for i in Total:
        print(i)
    print("Thankyou for using matrix calculator")


def Multiplication():
    m = int(input("Enter number of rows : "))
    n = int(input("Enter number of columns : "))
    matrix1 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix1 : ")))
        matrix1.append(x)
    print()
    matrix2 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix2 : ")))
        matrix2.append(x)
    print("matrix1: ")
    for i in matrix1:
        print(i)
    print("matrix2: ")
    for i in matrix2:
        print(i)

    Total = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(0)
        Total.append(x)
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                Total[i][j] += matrix1[i][k] * matrix2[k][j]
    print("Multiplication of both matrices")
    for i in Total:
        print(i)
    print("Thankyou for using matrix calculator")


def Subtraction():
    m = int(input("Enter number of rows : "))
    n = int(input("Enter number of columns : "))
    print()
    matrix1 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix1 : ")))
        matrix1.append(x)

    print()
    matrix2 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix2 : ")))
        matrix2.append(x)
    print("matrix1: ")
    for i in matrix1:
        print(i)
    print("matrix2: ")
    for i in matrix2:
        print(i)

    Total = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(0)
        Total.append(x)

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            Total[i][j] = matrix1[i][j] - matrix2[i][j]

    print("Substraction of both matrices: ")
    for i in Total:
        print(i)
    print("Thankyou for using matrix calculator")


import numpy as np


def Determinant():
    m = int(input("Enter number of rows : "))
    n = int(input("Enter number of columns : "))
    if n != m:
        print('for determinants matrix must have equal row and column')

    print()
    matrix1 = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements : ")))
        matrix1.append(x)
    print("matrix1")
    for i in matrix1:
        print(i)
    det = int((np.linalg.det(matrix1)) + 1)
    print("Determinant is :", det)
    print("Thankyou for using matrix calculator")


def symmetric():
    n = int(input("Enter the number of row or column"))
    matrix1 = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix1 : ")))
        matrix1.append(x)
    print("matrix1")
    for i in matrix1:
        print(i)
    total = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(0)
        total.append(x)
    for i in range(n):
        for j in range(n):
            total[i][j] = matrix1[j][i]
    print("Transpose of matrix1")
    for i in total:
        print(i)
    if total == a:
        print('symmetric')
    else:
        print('not symmetric')
    print("Thankyou for using matrix calculator")


def skewsymmetric():
    n = int(input("Enter the number of row or column"))
    matrix1 = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(int(input("Enter Elements for matrix1 : ")))
        matrix1.append(x)
    print("matrix1: ")
    for i in matrix1:
        print(i)
    total = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(0)
        total.append(x)
    for i in range(n):
        for j in range(n):
            total[i][j] = -matrix1[j][i]
    print("Negative of a Transpose of matrix1")
    for i in total:
        print(i)
    if total == a:
        print('skewsymmetric')
    else:
        print('not skewsymmetric')
    print("Thankyou for using matrix calculator")
    print("OK")


choice = int(input("Enter your choice : "))
if choice == 1:
    Addition()
elif choice == 2:
    Subtraction()
elif choice == 3:
    Multiplication()
elif choice == 4:
    Determinant()
elif choice == 5:
    symmetric()
elif choice == 6:
    skewsymmetric()
else:
    print("INVALID CHOICE !!!!!!!")


