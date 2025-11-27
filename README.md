# Sync_Heart_Cells_Simulation


## Introducción
Este codigo es una simulación de como las celulas del corazón se autoorganizan. Esta inspirado en el libro _"Sync,how order emerges from chaos in the universe, nature, and daily life"_ de Steven Strogatz.

## Dependencias y como ejecutar
### Librerías necesarias:
- **Numpy**: Para cálculos numéricos
- **Random**: Para randomizar las condiciones iniciales
- **Matplotlib**: Para graficar resultados
- **Pygame**: Para animar la representación de la simulación

### Ejecución del código
Para comenzar hay que entrar en el archivo **configuracion.py** y elegir el tipo de descarga y las condiciones de contorno de la simulación. (Las condiciones de contorno solo afectan al tipo de descarga local). Personalmente recomiendo empezar visualizando el tipo de descarga global.
A continuación es necesario ejecutar el archivo **Sync_Sim.py**.
Este archivo simula el proceso y genera 2 archivos: 
- **output.npy**: de unos 200MB, contiene la informacion de cada célula en cada iteracion del proceso
- **output_metrics.npy**: de unos 250KB, contiene información del conjunto (La carga media y la entropía de Shannon)

Una vez ejecutado y esos 2 archivos han sido creados se puede ejecutar **Sync_Sim_Visualizer.py** que abre una ventana 1280x720p donde se anima , para cada iteración, el estado de cada célula de la matriz y se representan en gráficas los valores de carga media y entropía de Shannon.
Durante el proceso genera y sobreescribe **plot_temp.png**.

## Explicación Simulación
Un conjunto de células reciben constantemente carga eléctrica, cuanta mas carga eléctrica tienen menos reciben. Al llegar a cierto valor de carga eléctrica las células se descargan de golpe, perdiendo toda la carga y dándosela al resto de células (todas o las próximas solo).
Para el caso en el que la descarga se realiza a las vecinas próximas es importante considerar como tratar las condiciones de contorno. Estas pueden ser periodicas (El borde de arriba es vecino del borde de abajo, lo mismo para los lados), fijas (Las células de los bordes tienen siempre carga 0) o una mezcla de ambas (Por ejemplo que los bordes superior e inferior tengan condiciones de contorno fijas y el resto periódicas)
Despues de ciertas iteraciones se puede observar como la entropía de Shannon del sistema disminuye y como la carga media pasa de un comportamiento caótico a un comportamiento ordenado con varias frecuencias, y pasado el tiempo se unifica en una única frecuencia, donde todas las células se comportan de manera sincronizada, como una única célula.


A


