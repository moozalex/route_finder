# Alex Moozhayil


from Node import Node
from Edge import Edge
import heapq


class Graph:
    """"This class creates a graph object."""
    def __init__(self):
        self.node_list = []
        self.edge_list = []
        self.node_set = set()
        self.adjacency_list = {}
        self.priority_queue = []
        self.path_list = {}

    def add_node(self, node: str):
        if node in self.node_set:
            return
        else:
            self.node_set.add(node)
            self.node_list.append(node)

    def add_edge(self, edge: Edge):
        self.edge_list.append(edge)

        """This is adding new keys to the adjacency list"""
        if edge.get_source() not in self.adjacency_list:
            self.adjacency_list[edge.get_source()] = []
            self.path_list[edge.get_source()] = []
        self.adjacency_list[edge.get_source()].append((edge.get_destination(), edge.edge_weight))
        self.path_list[edge.get_source()].append(edge.get_destination())
