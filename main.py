import csv
import numpy as np
import math as mt
import plotly
plotly.tools.set_credentials_file(username='AntonioMP', api_key='gkG6ymItx5uUmdKT46KA')
import plotly.plotly as py
import plotly.figure_factory as ff
import threading

def create_dendogram(matrix):  
    dendro = ff.create_dendrogram(matrix)
    dendro['layout'].update({'width':1366, 'height':768})
    py.iplot(dendro, filename='dendogram')


def get_pos_of_min_value(matrix, size):
    mm = matrix[0][1]
    p_x, p_y = 0, 1
    #paralelizar aqui
    for x in range(0, size):
        for y in range(x+1, size):
            if mm > matrix[x][y] and (x+1) < size:
                mm = matrix[x][y]
                p_x, p_y = x, y
    print('MENOR: ',mm)
    return p_x, p_y

def get_minimums(cluster1, cluster2, size, p_y):
    cluster_r = np.zeros(size)
    for x in range(0, size):
        cluster_r[x] = min(cluster1[x], cluster2[x])
    #print('---------------MINIMOS-----------------')
    cluster_r = np.delete(cluster_r, p_y)
    #print(cluster_r)
    return cluster_r

def do_union_of_clusters(matrix, p_x, p_y, size):
    col1 = np.zeros(size)
    col2 = np.zeros(size)
    print("---------------------CLUSTERS A UNIR-------------------------")
    print(p_x, p_y)
    for x in range(0, size):
        col1[x] = matrix[x][p_y]
        col2[x] = matrix[x][p_x]

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
    print("TAMA;O: ",n)
    cc = 0
    while n> 2:
        matrix, n = do_union_of_clusters(matrix, p_x, p_y, n)
        print("TAMA;O: ",n)
        p_x, p_y = get_pos_of_min_value(matrix, matrix.shape[0])
        cc += 1
    print('UNIONES: ',cc)
    return matrix

def create_distance_matrix(iris_matrix, iris_vector, dist_matrix, pos):
    # Generando datos de la matriz de distancia.
    for y in range (0, 150):
            # Formula ((X1 - X2)^2 + (Y1 - Y2)^2) + (Z1 - Z2)^2 + (W1 - W2)^2))^(1/2)
            p_x = iris_vector[0] - iris_matrix[y][0]
            p_y = iris_vector[1] - iris_matrix[y][1]
            s_x = iris_vector[2] - iris_matrix[y][2]
            s_y = iris_vector[3] - iris_matrix[y][3]
            # (W+X+Y+Z) ^(1/2)
            xy = pow(p_x, 2) + pow(p_y, 2) + pow(s_x, 2) + pow(s_y, 2)
            dist_matrix[pos][y] = mt.sqrt(xy)

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
    threads = []
    dist_matrix = np.zeros((150, 150))
    for i in range(150):
        t = threading.Thread(target=create_distance_matrix, args=(iris_matrix, iris_matrix[i], dist_matrix, i))
        threads.append(t)
        t.start()
    print('---------------------------MATRIZ DE DISTANCIA (IRIS)-----------------------------------')
    #create_dendogram(dist_matrix)
    for i in range(150):
        threads[i].join()
    print(dist_matrix)

    final = create_agglomerative_matrix(dist_matrix)
    print('---------------------------MATRIZ FINAL------------------------------')
    print(final)


main()