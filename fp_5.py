"""
Завдання 5. Візуалізація обходу бінарного дерева
Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

 👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

"""


import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(arr):
    heapq.heapify(arr)

    def build_node(idx):
        if idx >= len(arr):
            return None
        node = Node(arr[idx])
        node.left = build_node(2 * idx + 1)
        node.right = build_node(2 * idx + 2)
        return node

    return build_node(0)


def generate_color(step):
    colors = ['#0000ff', '#6363fc', '#9898fa', '#d7a6ff', '#b55aff', '#c500fc']

    idx = step % 6
    return colors[idx]


def dfs_visualization(root):
    stack = [root]
    step = 0
    while stack:
        node = stack.pop()
        node.color = generate_color(step)
        step += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def bfs_visualization(root):
    queue = deque([root])
    step = 0
    while queue:
        node = queue.popleft()
        node.color = generate_color(step)
        step += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    arr = [4, 0, 10, 3, 5, 1]
    root = build_heap_tree(arr)
    dfs_visualization(root)
    draw_tree(root)
    bfs_visualization(root)
    draw_tree(root)
