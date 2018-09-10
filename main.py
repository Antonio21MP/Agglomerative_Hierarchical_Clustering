import csv
import numpy as np
import math as mt

def get_pos_of_min_value(matrix, size):
    mm = matrix[0][1]
    p_x, p_y = 0, 1
    for x in range(0, size):
        for y in range(x+1, size):
            print("------------MM: ", mm, "------------------")
            if mm > dist_matrix[x][y] and (x+1) < size:
                mm = dist_matrix[x][y]
                p_x, p_y = x, y
    return p_x, p_y
## AQUI ESTA EL PROBLEMA TIENES QUE CAMBIAR QUE VARIABLES QUEDAN
def get_minimums(cluster1, cluster2, size, p_y):
    cluster_r = np.zeros(size)
    for x in range(0, size):
        cluster_r[x] = min(cluster1[x], cluster2[x])
    print('---------------MINIMO-----------------')
    cluster_r = np.delete(cluster_r, p_y)
    print(cluster_r)
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
    
    print("----------------R1-----------------")
    print(row1)
    print("----------------R2-----------------")
    print(row2)
    print("----------------C1-----------------")
    print(col1)
    print("----------------C2-----------------")
    print(col2)

    matrix = np.delete(matrix, (p_x), axis=0)
    matrix = np.delete(matrix, (p_y-1), axis=0)
    matrix = np.delete(matrix, (p_x), axis=1)
    matrix = np.delete(matrix, (p_y-1), axis=1)

    print("-------------MATRIX TEMPORAL-------------")
    cluster_u = get_minimums(col1, col2, size, p_y)
    tmp = np.zeros(size-2)
    matrix = np.insert(matrix, p_x, tmp, axis=0)
    tmp = np.zeros(size-1)
    matrix = np.insert(matrix, p_x, tmp, axis=1)
    print(matrix)

    print("-------------MATRIX FINAL-------------")
    matrix[p_x] = cluster_u
    for x in range(0, size-1):
        matrix[x][p_x] = cluster_u[x]
    print(matrix)
    return matrix, matrix.shape[0]

#------------------------------- MAIN ----------------------------------------#
'''
# Matriz de distancias para verficar si el algorithmo funciona.
dist_matrix = [ [0.00, 0.71, 5.66, 3.61, 4.24, 3.20],
                [-1, 0.00, 4.95, 2.92, 3.54, 2.50],
                [-1, -1, 0.00, 2.95, 3.54, 2.50],
                [-1, -1, -1, 0.00, 1.00, 0.50], 
                [-1, -1, -1, -1, 0.00, 1.12], 
                [-1, -1, -1, -1, -1, 0.00]]
#impresion en pantalla de la matriz de distancia.
print ("Matriz de Distancias")
print ("Dist A     B     C     D     E     F")
rows = ['A', 'B', 'C', 'D', 'E', 'F']
for x in range(0,6):
    print rows[x]," ", dist_matrix[x]
# posiciones de los cluster que tiene la menor distancia.
c_one, c_two = get_min_pos_in_matrix(dist_matrix)

print "Clusters {", c_one, c_two, "}"
# clusters a ser combinados en este caso resulta ser D y F
val_c_one = dist_matrix[c_one] 
val_c_two = dist_matrix[c_two]

print "C_one", val_c_one
print "C_two", val_c_two
'''
# Inicializando matrices petal y sepal
petal_data = np.zeros((150, 2))
sepal_data = np.zeros((150, 2))

# Llenando matriz petal
with open('data_set.csv') as File:
    iris_data = csv.DictReader(File)
    x = 0
    for row in iris_data:
        petal_data[x][0] = row['petal.length']
        petal_data[x][1] = row['petal.width']
        x += 1
   # print(petal_data)
# Lleando matriz sepal
with open('data_set.csv') as File:
    iris_data = csv.DictReader(File)
    x = 0
    for row in iris_data:
        sepal_data[x][0] = row['sepal.length']
        sepal_data[x][1] = row['sepal.width']
        x += 1
# Impresion de todos los datos originales de las matrices sepal y petal

'''
print('.-------------------PETAL--------------------.')
for row in range (0,150):
    print(petal_data[row][0], petal_data[row][1])
print('.-------------------SEPAL--------------------.')

for row in range (0,150):
    print(petal_data[row][0], petal_data[row][1])
'''
'''
#inicializando matriz de distancias
distance_matrix = np.empty((150, 150))
distance_matrix[:] = -1
# Formula ((X1 - X2)^2 + (Y1 - Y2)^2)^(1/2)
# Generando datos de la matriz de distancia.

for x in range (0, 150):
    for y in range(x, 150):
        t_x = petal_data[x][0] - petal_data[y][0]
        t_y = petal_data[x][1] - petal_data[y][1]
        xy = pow(t_x, 2) + pow(t_y, 2)
        distance_matrix[x][y] = mt.sqrt(xy)
'''
print('---------------------------MATRIZ DE DISTANCIA-----------------------------------')

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

p_x, p_y = get_pos_of_min_value(dist_matrix, dist_matrix.shape[0])
dis_matrix = do_union_of_clusters(dist_matrix, p_x, p_y, 6)
n = dist_matrix.shape[0]
print('--------------------N:',n, '-------------------------------')
while n> 2:
    dist_matrix, n = do_union_of_clusters(dist_matrix, p_x, p_y, n)
    print('--------------------N:',n, '------------------------------')
    p_x, p_y = get_pos_of_min_value(dist_matrix, dist_matrix.shape[0])

## Teniendo los dos valores realizar las operaciones siguientes min(3.61,3.20)
## y asi sucesivamente con los demas datos. Luego eliminar esos 2 cluster de la
## matriz de distancia y poner este nuevo cluster en la matriz de distancia.