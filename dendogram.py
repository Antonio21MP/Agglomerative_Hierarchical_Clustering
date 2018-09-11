import plotly
plotly.tools.set_credentials_file(username='AntonioMP', api_key='gkG6ymItx5uUmdKT46KA')
import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np

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
names = ['A','B','C','D','E','F']  
dendro = ff.create_dendrogram(dist_matrix, orientation='left', labels=names)
dendro['layout'].update({'width':800, 'height':500})
py.iplot(dendro, filename='iris')