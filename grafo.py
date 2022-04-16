import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import append
import menu as m

def rutaMasCorta():
    # Definir el número de nodos/vertices
    listaVertices = np.array([])
    cantVertices = int(input("Ingrese la cantidad de vertices de su grafo:  "))
    # Pedir cada nodos/vertices
    for i in range(cantVertices):
        vertice = input(f"Ingrese el nombre del vertice {i + 1}:  ")
        listaVertices = append(listaVertices, vertice)
    print(listaVertices)
    # Definir las aristas y el peso de cada arista
    # Inicializar las variables
    listaFilas = np.array([])
    listaColumnas = np.array([])
    listaPeso = np.array([])
    for v in range(cantVertices):
        cantAristas = int(input(f"Cuántos vertices son adyancentes a {listaVertices[v]}? "))
        for i in range(cantAristas):
            listaFilas = append(listaFilas, listaVertices[v])
            verticeUnion = input(f"Ingrese el vertice n{[i + 1]} que está unído al vertice {listaVertices[v]}:  ")
            listaColumnas = append(listaColumnas, verticeUnion)
            peso = int(input(f"Ingrese el peso de la arista ([{listaVertices[v]}, {verticeUnion}]):  "))
            listaPeso = append(listaPeso, peso)
    print(f"Fila= {listaFilas}")
    print(f"Columna= {listaColumnas}")
    print(f"Peso= {listaPeso}")

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






