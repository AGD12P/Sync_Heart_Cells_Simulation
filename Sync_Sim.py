import numpy as np
import random
import csv



def carga_natural(matriz,n):
    matriz += 2 - (1.85 * (matriz / 255)**2) #25/11/2025
    #matriz += 2 - (1.99 * (matriz / 255)**2)

    return matriz
"""
def descarga_natural(matriz,i,j):
    matriz += 50
    matriz[i,j]=0
    return matriz
"""
def descarga_natural(matriz,i,j): #25/11/2025 (No cambia nada creo)
    matriz += 50
    matriz[i,j]-= 255
    return matriz

def carga_artificial(matriz,n):
    #matriz += n/2 * (2 - (1.85 * (matriz / 255)**2))
    matriz += n/2 * (2 - (1.85 * (matriz / 255)**2))
    return matriz

def carga_artificial_local(matriz,i,j,n):
    def factor(matriz,i,j,n):
        return n/2 * (2 - (1.85 * (matriz[i,j] / 255)**2))
    
    #matriz += n/2 * (2 - (1.85 * (matriz / 255)**2))
    #Cond contorno periodicas
    i_sig = i+1
    i_ant = i-1

    j_sig = j+1
    j_ant = j-1

    if i == 0:
        i_ant = np.shape(matriz)[0]-1
    if i == np.shape(matriz)[0]-1:
        i_sig = 0
    if j == 0:
        j_ant = np.shape(matriz)[1]-1
    if j == np.shape(matriz)[1]-1:
        j_sig = 0
    I = [i_sig,i,i_ant]
    J = [j_sig,j,j_ant]
    for ii in I:
        for jj in J:
            if not (ii == i and jj == j):
            #if not (ii == i and jj == j) and ii != 0 and jj !=0:
                matriz[ii,jj] += factor(matriz,ii,jj,n)
                ###matriz[ii,jj] += factor(matriz,i,j,n)
                

    matriz[0,:]=0
    #matriz[:,0]=0
    matriz[np.shape(matriz)[0]-1,:]=0
    #matriz[:,np.shape(matriz)[1]-1]=0
    return matriz   

def entropia_de_shannon(matriz):
    matriz = np.round(matriz)
    H = 0
    for i in range(255):
        px = np.sum(matriz == i)/np.size(matriz)
        if px != 0:
            H -= px*np.log2(px)
    return H



X=50
Y=50
iteraciones = 10000

matriz = np.zeros([Y,X])
for i in range(Y):
    for j in range(X):
        matriz[i,j]=random.randint(0,255)
        #matriz[i,j]=random.randint(0,100)


iter_list = np.zeros((iteraciones, Y, X))
iter_metrics = np.zeros((iteraciones,3)) #

for it in range(iteraciones):
    iter_list[it] = matriz.copy()
    iter_metrics[it,0]=it
    iter_metrics[it,1]=np.sum(matriz)/(X*Y)
    iter_metrics[it,2]=entropia_de_shannon(matriz)
    matriz = carga_natural(matriz,1)
    c=0
    if it % 100 == 0:
            print('Iteraciones:',it)
    while np.any(matriz >= 255):
        c+=1
        ##print('While:',c)
            
        
        
        
        #matriz = carga_artificial(matriz,50)
        

        #25/11/2025 Descarga a las celulas vecinas
        """
        ij = np.where(matriz >= 255)
        ij = np.argmax(matriz >= 255)
        ij = np.unravel_index(ij, matriz.shape)
        matriz = carga_artificial_local(matriz,ij[0],ij[1],50)
        matriz[ij[0],ij[1]] = 0
        """
        
        

        # Descarga a todas las celudas
        ij = np.where(matriz >= 255)
        ij = np.argmax(matriz >= 255)
        ij = np.unravel_index(ij, matriz.shape)
        matriz = carga_artificial(matriz,52)
        matriz[matriz >= 255] = 0
        #matriz[ij[0],ij[1]] = 0
    

np.save(f'output.npy',iter_list)
np.save(f'output_metrics.npy',iter_metrics)
'''
with open('output.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(iter_list)'''
