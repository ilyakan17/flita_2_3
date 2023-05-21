from graphviz import Graph

def read_file(filename):
    adjacency_matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            adjacency_matrix.append(row)
    return adjacency_matrix

def visualize_graph(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    dot = Graph()
    # Добавление вершин графа
    for i in range(num_vertices):
        dot.node(str(i))
    # Добавление ребер графа
    for i in range(num_vertices):
        for j in range(i, num_vertices):
            weight = adjacency_matrix[i][j]
            if weight > 0:
                dot.edge(str(i), str(j), label=str(weight))
    # Вывод графа в формате PNG
    dot.render('graph', view=True)

def connection(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    max_edges = (num_vertices - 1) * (num_vertices - 2) // 2
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2
    return num_edges >= max_edges

def main():
    filename = input("Введите имя файла с матрицей смежности: ")
    adjacency_matrix = read_file(filename)
    visualize_graph(adjacency_matrix)

    if connection(adjacency_matrix):
        print("Граф связан")
    else:
        print("Граф не связан")

if __name__ == '__main__':
    main()
