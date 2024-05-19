import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.DiGraph()  # Використовуємо орієнтований граф для напрямку

# Додаємо станції метро як вузли
stations = [
    "Vokzalna",
    "Metrobudivnykiv",
    "Metalurhiv",
    "Zavodska",
    "Prospekt Svobody",
    "Pokrovska",
    "Teatralna",
    "Tsentralna",
    "Muzeina"
]

G.add_nodes_from(stations)

# Додаємо орієнтовані ребра з вагами
edges_with_weights = [
    ("Vokzalna", "Metrobudivnykiv", 5),
    ("Metrobudivnykiv", "Metalurhiv", 3),
    ("Metalurhiv", "Zavodska", 4),
    ("Zavodska", "Prospekt Svobody", 2),
    ("Prospekt Svobody", "Pokrovska", 6),
    ("Vokzalna", "Teatralna", 7),
    ("Teatralna", "Tsentralna", 8),
    ("Tsentralna", "Muzeina", 5)
]

G.add_weighted_edges_from(edges_with_weights)

# Встановлюємо позиції для вузлів, щоб вони були в лінію
pos = {
    "Vokzalna": (1.04, 1.01),
    "Metrobudivnykiv": (-0.2, 1.015),
    "Metalurhiv": (-1, 1.024),
    "Zavodska": (-2, 1.02),
    "Prospekt Svobody": (-3.02, 1.033),
    "Pokrovska": (-4.2, 1.03),
    "Teatralna": (1.8, 0.99),
    "Tsentralna": (3.1, 0.98),
    "Muzeina": (4, 0.97)
}

# Малюємо граф
plt.figure(figsize=(14, 8))

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)
nx.draw_networkx_labels(G, pos, font_size=15, font_color='black', font_weight='bold')

# Малюємо існуючі ребра
nx.draw_networkx_edges(G, pos, edgelist=edges_with_weights, edge_color='red', arrows=True, arrowstyle='-|>', arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d for u, v, d in edges_with_weights}, font_color='blue')

# Додаємо кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
plt.title(f"Мережа метро (Вершини: {num_nodes}, Ребра: {num_edges})")

plt.show()

# Алгоритм Дейкстри
def dijkstra(graph, start):
    return nx.single_source_dijkstra_path_length(graph, start)

# Знаходимо найкоротші шляхи між всіма вершинами
shortest_paths = {}
for station in stations:
    shortest_paths[station] = dijkstra(G, station)

# Виводимо найкоротші шляхи між всіма вершинами
for start, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від {start}:")
    for end, length in paths.items():
        print(f"  До {end}: {length}")
