import math
import numpy


def transposta(mat):
    i = 0
    j = 0
    col = len(mat[0]) #pega colunas
    lin = len(mat)
   # print(lin)
    results = numpy.zeros((lin,col))
    while i < col:
        while (j < lin):
         results[i][j]=mat[j][i]
         j = j + 1
    #     print(j)
        i = i + 1
        j=0  
    #    print('------')
     #   print(i)  
   # print(results)
    
#mat = [[1,2,3],[4,5,6],[7,8,9]]
#transposta(mat)

 
#exports.transposta= function(mat){
#//function  transposta(mat){
#    var dim = math.size(mat);//informa o tamanho da matriz
 #   var result = math.zeros(dim);
  #  for (var i = 0; i < dim[0]; i++) {
   #     for (var j = 0; j < dim[1]; j++) {
    #        result[i][j]=mat[j][i];
     #   }
    #}
  # // console.log(result)
	#return result;

#}
#//mat = [[1,2,3],[4,5,6],[7,8,9]];
#//transposta (mat);


