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

#Matriz de distancias.
dist_matrix = [ [0.00, 0.71, 5.66, 3.61, 4.24, 3.20],
                [0.71, 0.00, 4.95, 2.92, 3.54, 2.50],
                [5.66, 4.95, 0.00, 2.95, 3.54, 2.50],
                [3.61, 2.92, 2.24, 0.00, 1.00, 0.50], 
                [4.24, 3.54, 1.41, 1.00, 0.00, 1.12], 
                [3.20, 2.50, 2.50, 0.50, 1.12, 0.00]]
print ("Matriz de Distancias")
print ("Dist A     B     C     D     E     F")
rows = ['A', 'B', 'C', 'D', 'E', 'F']
for x in range(0,6):
    print rows[x]," ", dist_matrix[x]
c_one, c_two = get_min_pos_in_matrix(dist_matrix)

print "Clusters {", c_one, c_two, "}"

val_c_one = dist_matrix[c_one]
val_c_two = dist_matrix[c_two]

print "C_one", val_c_one
print "C_two", val_c_two
