from threading import Timer
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import append
import menu as m

def rutaMasCorta():
    # Datos quemados del Grafo del proyecto
    listaVertices = np.array(['R4', 'KL', 'JT', 'RG', 'H9', 'F7', 'X2', 'A4', 'A2', 'O9', 'O10', 'F4', 'H3', 'H5', 'R9', 'X1', 'T5', 'R5', 'R10', 'LL', 'U8', 'D4', 'U7', 'T6', 'E4', 'Y6'])
    listaFilas = np.array(['R4', 'KL', 'KL', 'JT', 'JT', 'RG', 'RG', 'H9', 'H9', 'F7', 'F7', 'X2', 'X2', 'A4', 'A4', 'A4', 'A2', 'A2', 'A2', 'A2', 'O9', 'O9', 'O9', 'O10', 'O10', 'F4', 'F4', 'F4', 'H3', 'H5', 'R9', 'R9', 'R9', 'X1', 'X1', 'X1', 'T5', 'T5', 'T5', 'R5', 'R5', 'R5', 'R5', 'R10', 'R10', 'LL', 'LL', 'U8', 'U8', 'U8', 'D4', 'D4', 'U7', 'T6', 'E4', 'Y6'])
    listaColumnas = np.array(['KL', 'R4', 'JT', 'KL', 'RG', 'H9', 'JT', 'RG', 'F7', 'H9', 'X2', 'F7', 'A4', 'X2', 'Y6', 'A2', 'A4', 'O9', 'O10', 'R9', 'A2', 'O10', 'F4', 'O9', 'A2', 'O9', 'H3', 'H5', 'F4', 'F4', 'A2', 'X1', 'R5', 'R9', 'E4', 'T5', 'X1', 'T6', 'R5', 'U8', 'R10', 'T5', 'R9', 'R5', 'LL', 'R10', 'U8', 'LL', 'R5', 'D4', 'U8', 'U7', 'D4', 'T5', 'X1', 'A4'])
    listaPeso = np.array([5, 5, 6, 6, 5, 4, 5, 4, 5, 5, 9, 9, 8, 8, 8, 7, 7, 8, 7, 6, 8, 7, 7, 7, 7, 7, 4, 6, 4, 6, 6, 6, 5, 6, 6, 7, 7, 4, 4, 3, 5, 4, 5, 5, 5, 5, 6, 6, 3, 5, 5, 3, 3, 4, 6, 8])
    
    # Generar gráfico no dirigido
    G = nx.Graph()  # Creación de un grafo vacío
    # Añadir un nodo al gráfico
    for i in range(0, np.size(listaVertices)):
        G.add_node(listaVertices[i])
    # Añadir bordes ponderados
    for i in range(0, np.size(listaFilas)):
        G.add_weighted_edges_from([(listaFilas[i], listaColumnas[i], listaPeso[i])])
    # Establecer diseño de red
    disenoG = nx.shell_layout(G)
    # Dibuja una imagen de red
    nx.draw(G, disenoG, with_labels=True, node_color='red', edge_color='blue', node_size=550, alpha=0.5)
    # Establece los atributos de nodos y bordes cuando networkx está dibujando (nombre vertices, peso arista...)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    # Une los atributos de nodos y bordes cuando networkx está dibujando
    nx.draw_networkx_edge_labels(G, disenoG, edge_labels)
    # Muestra los atributos de nodos y bordes cuando networkx está dibujando
    plt.show()
    
    # dijkstra método para encontrar el camino más corto con dijkstra_path
    inicio, final = input("Ingrese el nombres de los vectores de inicio y fin separados por espacios:").split()
    m.cuentaRegresiva()
    # Ruta más corta con nodos
    rutaMasCorta = nx.dijkstra_path(G, source=inicio, target=final, weight='weight')
    print("Ruta más corta: ", rutaMasCorta)
    # Creamos un gráfo desde rutaMasCorta
    rutaG = nx.path_graph(rutaMasCorta)
    # Ruta más corta con aristas
    print("Lista de aristas que forman el camino más corto:")
    # Ciclo para imprimir cada arista que conforma la ruta más corta del gráfo G
    for i in rutaG.edges():
        print(i)

    # Se suma el peso de cada arista de la ruta más corta
    distanciaMasCorta = nx.dijkstra_path_length(G, source=inicio, target=final)
    print('La distancia más corta desde el vector {0} a {1} es de:'.format(inicio, final), distanciaMasCorta)