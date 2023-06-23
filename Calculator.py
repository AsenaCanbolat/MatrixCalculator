print("Select operation.")
print("1.Add two matrices")
print("2.Subtract two matrices")
print("3.Multiply two matrices")
print("4.Multiply matrix by a constant")
print("5.Transpose of matrix")
print("6.Determinant")


def empty_matrix(row, col):
    ResultM = [[0 for _ in range(col)] for _ in range(row)]
    return ResultM

def determinantCalculator(inputMatrix):
   
    # 1x1 matrix
    if len(inputMatrix) == 1:
        return inputMatrix[0][0]
   
    # 2x2 matrix
    if len(inputMatrix) == 2 and len(inputMatrix[0]) == 2:
        return inputMatrix[0][0] * inputMatrix[1][1] - inputMatrix[0][1] * inputMatrix[1][0]

    determinant = 0
    sign = 1
   
    # Iterasyon for larger matrix
    for col in range(len(inputMatrix[0])):
        sub_matrix = []
        # İlk satır ve geçerli sutun çıkarılarak alt matris olustur
        for i in range(1, len(inputMatrix)):
            sub_matrix.append(inputMatrix[i][:col] + inputMatrix[i][col + 1:])
        determinant += sign * inputMatrix[0][col] * determinantCalculator(sub_matrix)
        sign *= -1
    return determinant

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice == '1':
        print("IMPORTANT:Addition happens only between matrices of the same size.")
    elif choice == '2':
        print("IMPORTANT:Subtraction happens only between matrices of the same size.")
    elif choice == '3':
        print(
            "IMPORTANT:Multiplication happens only if the first matric's column size is equal to second matric's row size.")
    elif choice == '6':
        print("IMPORTANT:Calculation of the matric's determinant possible only in square matrices.")

    # check if choice is one of the six options
    if choice in ('5', '6'):

        try:
            # define the range of rows and colums
            row1 = int(input("Enter the number of rows: "))
            col1 = int(input("Enter the number of columns: "))

            Matrix = []  # for creating a blank matrix
            for i in range(0, row1):
                Matrix.append([])

            for i in range(0, row1):
                for j in range(0, col1):
                    Matrix[i].append(j)
                    Matrix[i][j] = 0

            for i in range(0, row1):
                for j in range(0, col1):
                    print('Enter the value of ', i + 1, '. row:', ' and ', j + 1, '. column:')
                    Matrix[i][j] = int(input())

        except ValueError:
            print("Invalid input. Please enter again.")
            continue

    elif choice in ('4'):

        try:

            # define the 1. matrix's range of rows and colums
            row1 = int(input("Enter the number of rows: "))
            col1 = int(input("Enter the number of columns: "))

            Matrix = []  # for creating a blank matrix
            for i in range(0, row1):
                Matrix.append([])

            for i in range(0, row1):
                for j in range(0, col1):
                    Matrix[i].append(j)
                    Matrix[i][j] = 0

            for i in range(0, row1):
                for j in range(0, col1):
                    print('Enter the value of ', i + 1, '. row:', ' and ', j + 1, '. column:')
                    Matrix[i][j] = int(input())

            c = float(input('Enter the constant: '))

        except ValueError:
            print("Invalid input. Please enter again.")
            continue

    elif choice in ('1', '2', '3'):

        try:

            # define the 1. matrix's range of rows and colums
            row1 = int(input("Enter the number of rows: "))
            col1 = int(input("Enter the number of columns: "))

            Matrix = []  # for creating a blank matrix
            for i in range(0, row1):
                Matrix.append([])

            for i in range(0, row1):
                for j in range(0, col1):
                    Matrix[i].append(j)
                    Matrix[i][j] = 0

            for i in range(0, row1):
                for j in range(0, col1):
                    print('Enter the value of ', i + 1, '. row:', ' and ', j + 1, '. column:')
                    Matrix[i][j] = int(input())

            # define 2.matrix's range of rows and colums
            row2 = int(input("Enter the number of rows: "))
            col2 = int(input("Enter the number of columns: "))

            Matrix2 = []  # for creating a blank matrix
            for i in range(0, row2):
                Matrix2.append([])

            for i in range(0, row2):
                for j in range(0, col2, ):
                    Matrix2[i].append(j)
                    Matrix2[i][j] = 0

            for i in range(0, row2):
                for j in range(0, col2, ):
                    print('Enter the value of ', i + 1, '. row:', ' and ', j + 1, '. column:')
                    Matrix2[i][j] = int(input())

        except ValueError:
            print("Invalid input. Please enter again.")
            continue

    if choice in ('1', '2', '3', '4', '5', '6'):

        if choice == '1':
            ResultM = empty_matrix(len(Matrix), len(Matrix[0]))

            for i in range(row1):
                for j in range(col1):
                    for k in range(row2):
                        for l in range(col2):
                            if i == k and j == l:
                                ResultM[i][l] = Matrix[i][j] + Matrix2[k][l]
            
            print(Matrix, '+', Matrix2, '=',ResultM)


        elif choice == '2':

            ResultM = empty_matrix(len(Matrix), len(Matrix[0]))

            for i in range(row1):
                for j in range(col1):
                    for k in range(row2):
                        for l in range(col2):
                            if i == k and j == l:
                                ResultM[i][j] = Matrix[i][j] - Matrix2[k][l]

            print(Matrix, '-', Matrix2, '=',ResultM)

        elif choice == '3':

            ResultM = empty_matrix(len(Matrix), len(Matrix[0]))

            for i in range(row1):
                for j in range(col2):
                    for k in range(col1):
                        ResultM[i][j] += Matrix[i][k] * Matrix2[k][j]

            print((Matrix), 'x', (Matrix2), '=',ResultM)

        elif choice == '4':

            ResultM = empty_matrix(len(Matrix), len(Matrix[0]))

            for i in range(row1):
                for j in range(col1):
                    ResultM[i][j] = c * Matrix[i][j]

            print(Matrix, 'x', c, '=',ResultM)

        elif choice == '5':

            ResultM = empty_matrix(len(Matrix), len(Matrix[0]))

            for i in range(row1):
                for j in range(col1):
                    ResultM[i][j] = Matrix[j][i]

            print(Matrix, '^T = ',ResultM)

        elif choice == '6':

            #ResultM = empty_matrix(len(Matrix), len(Matrix[0]))

            if row1 == col1:
                determinant = determinantCalculator(Matrix)
                print("Determinant of the ",Matrix,' = ',determinant)
           
            else:
                print("Only the square matrices's determinant can be calculated.")

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no" or next_calculation == 'No'  or next_calculation == 'NO':
        break
    else:
        print("Invalid Input")
