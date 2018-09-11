import csv
import numpy as np
import math as mt

def get_pos_of_min_value(matrix, size):
    mm = matrix[0][1]
    p_x, p_y = 0, 1
    for x in range(0, size):
        for y in range(x+1, size):
            #print("------------MM: ", mm, "------------------")
            if mm > matrix[x][y] and (x+1) < size:
                print('MM:',mm)
                print('Menor:',matrix[x][y])
                mm = matrix[x][y]
                print('x: ',x,'y: ',y)
                p_x, p_y = x, y

    return p_x, p_y
## AQUI ESTA EL PROBLEMA TIENES QUE CAMBIAR QUE VARIABLES QUEDAN
def get_minimums(cluster1, cluster2, size, p_y):
    cluster_r = np.zeros(size)
    for x in range(0, size):
        cluster_r[x] = min(cluster1[x], cluster2[x])
    #print('---------------MINIMOS-----------------')
    cluster_r = np.delete(cluster_r, p_y)
    #print(cluster_r)
    return cluster_r

def do_union_of_clusters(matrix, p_x, p_y, size):
    row1 = matrix[p_x]
    row2 = matrix[p_y]
    col1 = np.zeros(size)
    col2 = np.zeros(size)
    print("---------------------X AND Y-------------------------")
    print(p_x, p_y)
    for x in range(0, size):
        col1[x] = matrix[x][p_y]
        col2[x] = matrix[x][p_x]
    '''
    print("----------------R1-----------------")
    print(row1)
    print("----------------R2-----------------")
    print(row2)
    print("----------------C1-----------------")
    print(col1)
    print("----------------C2-----------------")
    print(col2)
    '''
    matrix = np.delete(matrix, (p_x), axis=0)
    matrix = np.delete(matrix, (p_y-1), axis=0)
    matrix = np.delete(matrix, (p_x), axis=1)
    matrix = np.delete(matrix, (p_y-1), axis=1)

    cluster_u = get_minimums(col1, col2, size, p_y)
    tmp = np.zeros(size-2)
    matrix = np.insert(matrix, p_x, tmp, axis=0)
    tmp = np.zeros(size-1)
    matrix = np.insert(matrix, p_x, tmp, axis=1)
    #print("-------------MATRIX TEMPORAL-------------")
    #print(matrix)

    print("-------------MATRIZ RESULTANTE-------------")
    matrix[p_x] = cluster_u
    for x in range(0, size-1):
        matrix[x][p_x] = cluster_u[x]
    print(matrix)

    return matrix, matrix.shape[0]

def create_agglomerative_matrix(matrix):
    p_x, p_y = get_pos_of_min_value(matrix, matrix.shape[0])
    n = matrix.shape[0]
    print('--------------------TAMA;O:',n,'-------------------------------')
    while n> 2:
        matrix, n = do_union_of_clusters(matrix, p_x, p_y, n)
        print('--------------------TAMA;O:',n, '------------------------------')
        p_x, p_y = get_pos_of_min_value(matrix, matrix.shape[0])
    return matrix

def main():
    #------------------------------- MAIN ----------------------------------------#
    # Inicializando matriz iris
    iris_matrix = np.zeros((150, 4))
    # Llenando matriz petal
    with open('data_set.csv') as File:
        iris_data = csv.DictReader(File)
        x = 0
        for row in iris_data:
            iris_matrix[x][0] = row['petal.length']
            iris_matrix[x][1] = row['petal.width']
            iris_matrix[x][0] = row['sepal.length']
            iris_matrix[x][1] = row['sepal.width']
            x += 1


    #inicializando matriz de distancias
    dist_matrix = np.zeros((150, 150))

    # Generando datos de la matriz de distancia.
    for x in range (0, 150):
        for y in range(0, 150):
            # Formula ((X1 - X2)^2 + (Y1 - Y2)^2) + (Z1 - Z2)^2 + (W1 - W2)^2))^(1/2)
            p_x = iris_matrix[x][0] - iris_matrix[y][0]
            p_y = iris_matrix[x][1] - iris_matrix[y][1]
            s_x = iris_matrix[x][2] - iris_matrix[y][2]
            s_y = iris_matrix[x][3] - iris_matrix[y][3]
            # (W+X+Y+Z) ^(1/2)
            xy = pow(p_x, 2) + pow(p_y, 2) + pow(s_x, 2) + pow(s_y, 2)
            dist_matrix[x][y] = mt.sqrt(xy)
    print('---------------------------MATRIZ DE DISTANCIA (IRIS)-----------------------------------')
    print(dist_matrix)
    '''
    print('.-------------------IRIS--------------------.')
    for row in range (0,150):
        print(iris_matrix[row][0], iris_matrix[row][1], iris_matrix[row][2], iris_matrix[row][3])
    print('---------------------------MATRIZ DE DISTANCIA (PRUEBA)-----------------------------------')
    # Matriz de pruebas
    dist_matrix = np.zeros((6, 6))
    dist_matrix2 = [ [0.00, 0.71, 5.66, 3.61, 4.24, 3.20],
                    [0.71, 0.00, 4.95, 2.92, 3.54, 2.50],
                    [5.66, 4.95, 0.00, 2.24, 1.41, 2.50],
                    [3.61, 2.92, 2.24, 0.00, 1.00, 0.50], 
                    [4.24, 3.54, 1.41, 1.00, 0.00, 1.12], 
                    [3.20, 2.50, 2.50, 0.50, 1.12, 0.00]]
    for x in range(0, 6):
        for y in range(0, 6):
            dist_matrix[x][y] = dist_matrix2[x][y] 
    
    print(dist_matrix)
    '''
    final = create_agglomerative_matrix(dist_matrix)
    #dis_matrix, n = do_union_of_clusters(dist_matrix, p_x, p_y, dist_matrix.shape[0])
    #final_matrix = create_agglomerative_matrix(dis_matrix, p_x, p_y)
    print('---------------------------MATRIZ FINAL------------------------------')
    print(final)

    ## Teniendo los dos valores realizar las operaciones siguientes min(3.61,3.20)
    ## y asi sucesivamente con los demas datos. Luego eliminar esos 2 cluster de la
    ## matriz de distancia y poner este nuevo cluster en la matriz de distancia.
    # Impresion de todos los datos originales de las matrices sepal y petal


main()