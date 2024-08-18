def mult_mat_vet(mat, vet):
    result = []
    if len(mat[0]) == len(vet) or len(mat) == len(vet):
        for j in range(len(vet)):
            result.append(0)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result[j] += mat[i][j] * vet[i]
    else:
        print("vetores com tamanhos diferentes func mult_mat_vet aaa")
        
    return result
### OK ###

#mat = [[0.2101179, 0.12604131, 0.05775615, 0.01901292,0.0044964,  0.0008123 ],
# [0.16824926, 0.15740655, 0.11249362, 0.05775615 ,0.02130266 ,0.00600212],
# [0.08638205, 0.12604131, 0.14048753, 0.11249362 ,0.06471177 ,0.02843637],
# [0.02843637, 0.06471177, 0.11249362, 0.14048753 ,0.12604131 ,0.08638205],
# [0.00600212, 0.02130266, 0.05775615, 0.11249362 ,0.15740655 ,0.16824926],
# [0.0008123,  0.0044964 , 0.01901292, 0.05775615 ,0.12604131 ,0.2101179 ]]

#vet = [0, 0, 0, 0, 1, 0]

#print(mult_mat_vet(mat,vet))