import numpy as np

if __name__ == '__main__':

    M1 = [[1, 2, 3, 4, 11],
          [5, -6, 7, 8, 11],
          [5, 2, -42, 8, 11],
          [1, 6, 7, 11, 100]]

    rows = len(M1)
    columns = len(M1[0])
    # TODO print ALL elements of matrix
    print('M1:')
    for i in range(rows):
        for j in range(columns):
            print(M1[i][j],end = " ")
        print (' ')
    print('==========')
    print('M2:')
    M2 = [[1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    rows1 = len(M2[0])
    columns1 = len(M2)

    # TODO print diagonal - 1,-6,5,11
    for i in range(rows1):
        print(M2[i][i], end=" ")
    print(' ')
    print('==========')
    M3 =np.array (
        [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]])
    # TODO print diagonal in oposite order  4, 3, 2, 1
    #print(M3[:, ::-1])

    my_diag = M3.diagonal()
    my_dia1=list(my_diag)

    reversed_array = my_diag[::-1]
    print('M3:')
    print(reversed_array)





#x=int(str(x)[::-1])





