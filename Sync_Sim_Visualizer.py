import pygame, sys, os
import numpy as np
import random
import matplotlib.pyplot as plt
import configuracion


tipo_descarga = configuracion.tipo_descarga
condiciones_contorno = configuracion.condiciones_contorno

FPS = 180
ancho_ventana, alto_ventana = 1280, 720



data = np.load('output.npy', allow_pickle=True)
metrics = np.load('output_metrics.npy', allow_pickle=True)


print(np.shape(data))

#'''
pygame.init()
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Sync_Sim_Visualizer")
mainClock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 30)

it = 0
inicio = False
cont = 0


class cell(pygame.sprite.Sprite):
    def __init__(self, y, x, Q):
        super().__init__()
        self.x = x
        self.y = y
        self.width=10
        self.height=10
        self.Q=Q
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill([int(self.Q),0,0])
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)
    def update(self,Q):
        self.Q = Q
        self.image.fill([int(self.Q),0,0])
        self.rect = self.image.get_rect()
        self.rect.topleft=(self.x,self.y)
all_sprites = pygame.sprite.Group()
cells=[]

colorn = (25/255,25/255,25/255)
colorb = (200/255,200/255,200/255)
colorp1 = (255/255,255/255,0/255)
colorp2 = (255/255,127/255,39/255)
fig,ax = plt.subplots(2,1,figsize=(6,6))
fig.patch.set_facecolor((25/255,25/255,25/255))
ax[0].set_facecolor((127/255,127/255,127/255))
ax[1].set_facecolor((127/255,127/255,127/255))

temp_dir = 'temp_plot'
os.makedirs(temp_dir, exist_ok=True)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if inicio == False:
        for i in range(np.shape(data)[1]):
            for j in range(np.shape(data)[2]):
                cel = cell(11*i+64,11*j+64,data[it,i,j])
                all_sprites.add(cel)
                cells.append(cel)
        inicio = True

    
    if it >= len(data)-1:
        it=0
    else:
        it+=1
    
    if cont == 0:
        cont = 20

        ax[0].clear()
        ax[0].plot(metrics[0:it,0],metrics[0:it,1], color = colorp1, linewidth=0.7)
        ax[0].set_xlim(0, len(data))
        ax[0].set_ylim(-1, 256)
        #ax[0].set_xlabel('iteraciones', fontsize=14)
        ax[0].set_ylabel('Carga media', fontsize=14, color = colorb, fontname='monospace')
        ax[0].tick_params(axis='x', colors=colorb) 
        ax[0].tick_params(axis='y', colors=colorb)

        ax[1].clear()
        ax[1].plot(metrics[0:it,0],metrics[0:it,2], color = colorp2, linewidth=0.7)
        print(metrics[it,2])
        ax[1].set_xlim(0, len(data))
        ax[1].set_ylim(np.min(metrics[:,2])-2, 1.2*np.max(metrics[:,2]))
        ax[1].set_xlabel('iteraciones', fontsize=14, color=colorb,fontname='monospace')
        ax[1].set_ylabel('Entropia de Shannon', fontsize=14, color=colorb,fontname='monospace')
        ax[1].tick_params(axis='x', colors=colorb) 
        ax[1].tick_params(axis='y', colors=colorb)
        

        plot_file_path = "./plot_temp.png"
        fig.savefig(plot_file_path, format='png')
        plot_surface = pygame.image.load(plot_file_path)
    cont -= 1



    #all_sprites.update()
    #print(data[it,i,j])

    
    screen.fill((25, 25, 25))
    text = font.render(str(it)+''+'/'+''+str(len(data)), True, (255, 255, 255))
    text_info = font.render(str(tipo_descarga)+' '+'Condiciones '+str(condiciones_contorno), True, (255, 255, 255))
    #all_sprites.draw(screen)
    for i in range(np.shape(data)[1]):
            for j in range(np.shape(data)[2]):
                pygame.draw.rect(screen,[data[it,i,j],0,0],pygame.Rect(11*j+64,11*i+64,10,10))
                #celu = cells[i*np.shape(data)[1]+j]
                #celu.update(data[it,i,j])
    screen.blit(text, (20, 20))
    screen.blit(text_info, (200, 20))
    screen.blit(plot_surface, (650, 20))
    pygame.display.update()
    mainClock.tick(FPS)
#'''
