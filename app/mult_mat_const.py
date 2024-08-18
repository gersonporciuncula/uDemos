import numpy

def mult_mat_const(mat, value):
   
    i = 0
    j = 0
    col = len(mat[0]) #pega colunas
    lin = len(mat)
  #  print(lin)
    result = numpy.zeros((lin,col))
    while i < col:
        while (j < lin):
           result[i][j]=mat[i][j]*value
           j = j + 1
        i = i + 1
        j=0  
    return result
#mat = [[1,2,3],[4,5,6],[7,8,9]]
#value = 0.5
#print(mult_mat_const(mat, value))