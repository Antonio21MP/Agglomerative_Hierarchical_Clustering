import csv
import numpy as np
import math as mt
# funcion para obtener la resta de los valores de cada cluster en la primera columna de cada
# uno de ellos.
def get_sub_matrix(matrix):
    sub_matrix = list()
    for x in range(0,6):
        sub_vector = list()
        for x2 in range(0,6):
            sub = matrix[x][0] - matrix[x2][0]
            if sub < 0:
                sub *= -1 
            sub_vector.append(sub)
        sub_matrix.append(sub_vector)
    return sub_matrix

# funcion para obtener las posiciones en la matriz donde esta el valor min en toda la matriz
# esta funcion es necesaria para realizar unir dos clusters y luego determinar que datos de cada
# cluster seran los que se quedaran en el cluster combinado.
def get_min_pos_in_matrix(matrix):
    min_dist_matrix = get_sub_matrix(matrix)
    min_dist_matrix_2 = get_sub_matrix(matrix)
    
    for x in range(0,6):
        min_dist_matrix_2[x].remove(0.00)
    min_box = list()
    
    for x in range(0,6):
        mini =  min(min_dist_matrix_2[x])
        min_box.append(mini)
    pos_x = 0.00
    pos_y = 0.00
    for x in range(0,6):
        #print(x)
        try: 
            pos_x = min_dist_matrix[x].index(min(min_box))
        except:
            pos_x = -1
        if(pos_x != -1):
            pos_y = x
            break
    return pos_x, pos_y

#------------------------------- MAIN ----------------------------------------#
'''
# Matriz de distancias para verficar si el algorithmo funciona.
dist_matrix = [ [0.00, 0.71, 5.66, 3.61, 4.24, 3.20],
                [0.71, 0.00, 4.95, 2.92, 3.54, 2.50],
                [5.66, 4.95, 0.00, 2.95, 3.54, 2.50],
                [3.61, 2.92, 2.24, 0.00, 1.00, 0.50], 
                [4.24, 3.54, 1.41, 1.00, 0.00, 1.12], 
                [3.20, 2.50, 2.50, 0.50, 1.12, 0.00]]
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
    print(petal_data)
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
#inicializando matriz de distancias
distance_matrix = np.zeros((150, 150))

# Formula ((X1 - X2)^2 + (Y1 - Y2)^2)^(1/2)
# Generando datos de la matriz de distancia.
for x in range (0, 150):
    for y in range(x, 150):
        t_x = petal_data[x][0] - petal_data[y][0]
        t_y = petal_data[x][1] - petal_data[y][1]
        xy = pow(t_x, 2) + pow(t_y, 2)
        distance_matrix[x][y] = mt.sqrt(xy)
print('---------------------------MATRIZ DE DISTANCIA-----------------------------------')
print(distance_matrix[0])

    
## Teniendo los dos valores realizar las operaciones siguientes min(3.61,3.20)
## y asi sucesivamente con los demas datos. Luego eliminar esos 2 cluster de la
## matriz de distancia y poner este nuevo cluster en la matriz de distancia.