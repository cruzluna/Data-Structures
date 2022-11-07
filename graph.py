import pprint
from collections import defaultdict, namedtuple

# G = (V, E)
Graph = namedtuple("Graph", ["vertices", "edges"])

nodes = ["A", "B", "C", "D"]

edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D"),
]

G = Graph(nodes, edges)

pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(G)

def adjacency_dict(graph):
    """
    returns the adjaceny list representatino of graph

    Args:
        graph (_type_): _description_
    """
    adj_list = {node : [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    return adj_list

def adjaceny_matrix(graph):
    """
    return adjaceny matrix of the graph

    Args:
        graph (_type_): assumes that graph.nodes are equivalent to range(len(graph.nodes))
    """
    adj_matrix = [[0 for node in graph.nodes] for node in graph.nodes]

    for edge in edges: 
        #iterate through edges and increment edge connections
        node1, node2 = edge[0],edge[1]
        
        adj_matrix[node1][node2]+=1
        adj_matrix[node2][node1]+=1
        
    return adj_matrix
        