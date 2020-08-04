# Alex Moozhayil


from Node import Node


class Edge:
    """This class creates an edge object."""
    def __init__(self, source: str, destination: str, weight: int):
        self.node_source = source
        self.node_destination = destination
        self.edge_weight = weight

    def get_source(self):
        return self.node_source

    def get_destination(self):
        return self.node_destination

    def get_weight(self):
        return self.edge_weight
