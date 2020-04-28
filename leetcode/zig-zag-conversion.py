from __future__ import print_function
str = 'PAYPALISHIRING'
steps = len(str)
max_row_count = 3
no_columns = len(str)
no_rows = max_row_count - 1
matrix = []
for row in range(0, max_row_count):
    matrix2 = []
    for col in range(0, no_columns):
        matrix2.append(0)
    matrix.append(matrix2)

init_row_count = 0
init_col_count = 0
count = 0
while(count < steps):
    if(init_row_count == 0):
        while(init_row_count < max_row_count and count < steps):
            matrix[init_row_count][init_col_count] = str[count]
            count+=1
            init_row_count += 1
        init_row_count -= 1
        print('long down',init_row_count, init_col_count)
    elif (init_row_count == 1):
        init_row_count -= 1
        init_col_count += 1
    else:
        init_row_count -= 1
        init_col_count += 1
        matrix[init_row_count][init_col_count] = str[count]
        count+=1
        print('small up', init_row_count, init_col_count)
ansString = ''
for row in range(0, max_row_count):
    for col in range(0, no_columns):
        if(matrix[row][col] != 0):
            ansString += matrix[row][col]
        # print(matrix[row][col],end="")
    # print("")
print(ansString)