# Sync_Heart_Cells_Simulation


## Introducción
Este codigo es una simulación de como las celulas del corazón se autoorganizan. Esta inspirado en el libro _"Sync,how order emerges from chaos in the universe, nature, and daily life"_ de Steven Strogatz

## Dependencias y como ejecutar
- **Numpy**: Para cálculos numéricos
- **Random**: Para randomizar las condiciones iniciales
- **Matplotlib**: Para graficar resultados
- **Pygame**: Para animar la representación de la simulación

Primero es necesario ejecutar el archivo **Sync_Sim.py**.
Este archivo simula el proceso y genera 2 archivos: 
- **output.npy**: de unos 200MB, contiene la informacion de cada célula en cada iteracion del proceso
- **output_metrics.npy**: de unos 250KB, contiene información del conjunto (La carga media y la entropía de Shannon)

Una vez ejecutado y esos 2 archivos han sido creados se puede ejecutar **Sync_Sim_Visualizer.py** que abre una ventana 1280x720p donde se anima , para cada iteración, el estado de cada célula de la matriz y se representan en gráficas los valores de carga media y entropía de Shannon.
Durante el proceso genera y sobreescribe **plot_temp.png**.

## Explicación Simulación
