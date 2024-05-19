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

# Додаємо орієнтовані ребра, що представляють напрям лінії метро між станціями
existing_edges = [
    ("Vokzalna", "Metrobudivnykiv"),
    ("Metrobudivnykiv", "Metalurhiv"),
    ("Metalurhiv", "Zavodska"),
    ("Zavodska", "Prospekt Svobody"),
    ("Prospekt Svobody", "Pokrovska")
]

building_edges = [
    ("Vokzalna", "Teatralna"),
    ("Teatralna", "Tsentralna"),
    ("Tsentralna", "Muzeina")
]

G.add_edges_from(existing_edges)
G.add_edges_from(building_edges)

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
nx.draw_networkx_edges(G, pos, edgelist=existing_edges, edge_color='red', arrows=True, arrowstyle='-|>', arrowsize=20)
# Малюємо нові ребра, що будуються, пунктирними
nx.draw_networkx_edges(G, pos, edgelist=building_edges, edge_color='red', style='dashed', arrows=True, arrowstyle='-|>', arrowsize=20)

# Додаємо кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
plt.title(f"Мережа метро (Вершини: {num_nodes}, Ребра: {num_edges})")

plt.show()
