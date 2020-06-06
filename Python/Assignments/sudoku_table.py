sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

print('- '*11)
for j, satir_sudoku in enumerate(sudoku):
    #print('|', end=' ')
    for i,n in enumerate(satir_sudoku):
        if (i+1)%3==0 and i+1!= 9:
            print(n,'|', end=' ')
        else:
            print(n, end=' ')
    if (j+1)%3==0:
        print('\n'+'- '*11, end='')
    print(end='\n')    


