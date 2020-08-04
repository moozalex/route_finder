# Alex Moozhayil


import sys
from Graph import Graph
from Node import Node
from Edge import Edge
import heapq


def make_graph(filename):
    """

    :param filename: successor function file
    :return: returns a graph.
    """
    line = " "
    graph = Graph()

    with open(filename) as file_object:
        while line != "END OF INPUT\n":
            for line in file_object:
                if line == "END OF INPUT\n":
                    break
                else:
                    temp = line.split()

                    node1 = temp[0]
                    node2 = temp[1]
                    weight = int(temp[2])
                    edge_created = Edge(node1, node2, weight)
                    edge_created1 = Edge(node2, node1, weight)

                    graph.add_node(node1)
                    graph.add_node(node2)
                    graph.add_edge(edge_created)
                    graph.add_edge(edge_created1)

    return graph


def heuristic_info(filename):
    """

    :param filename: heurisitic file
    :return: returns a list of all the information that was in the heurisitic file
    """
    line = " "

    heuristic_list = {}

    with open(filename) as file_object:
        while line != "END OF INPUT\n":
            for line in file_object:
                if line == "END OF INPUT\n":
                    break
                else:
                    temp = line.split()
                    heuristic_list[temp[0]] = temp[1]
    return heuristic_list


def A_star(origin, destination, file, heuristic_file):
    """

    :param origin: the start destination
    :param destination: the final destination
    :param file: the successor function. input.txt
    :param heuristic_file: the heuristic file
    :return: outputs all the information. nodes expanded, generated, max nodes, distance, and route.
    """

    graph = make_graph(file)
    generated = 0
    expanded = 0
    path = []
    visited = []
    max_nodes = 0
    heuristic_list = heuristic_info(heuristic_file)
    path.append(origin)
    succ = graph.adjacency_list[origin]


    """This is going through the list of successors, one-by-one. Then, the successors are pushed onto the heap."""
    for location in succ:
        new = location[1] + int(heuristic_list[location[0]])
        heapq.heappush(graph.priority_queue, (new, location))
        generated += 1

    visited.append(origin)
    expanded += 1
    max_nodes = len(graph.priority_queue)

    flag = False
    cumm_weight = 0


    while len(graph.priority_queue) != 0:
        """we are popping a tuple, and checking the indices 0 - the destination"""
        current_destination = heapq.heappop(graph.priority_queue)[-1]
        expanded += 1

        if current_destination[0] in graph.path_list[path[-1]]:
            path.append(current_destination[0])

        if current_destination[0] == destination:
            flag = True
            cumm_weight = current_destination[1]
            break

        succ = graph.adjacency_list[current_destination[0]]

        if current_destination[0] not in visited:
            for location in succ:
                    cumm_weight = current_destination[1] + location[1]
                    f_of_n = current_destination[1] + int(heuristic_list[current_destination[0]])
                    heapq.heappush(graph.priority_queue, (f_of_n, (location[0], cumm_weight)))
                    generated += 1
            visited.append((current_destination[0]))

        if len(graph.priority_queue) > max_nodes:
            max_nodes = len(graph.priority_queue)

    if flag:
        print("nodes expanded: " + str(expanded))
        print("nodes generated: " + str(generated))
        print("max nodes in memory: " + str(max_nodes))
        print("distance: " + str(cumm_weight) + " km")
        print(origin + " to " + destination + ": " + str(cumm_weight) + " km")

    else:
        print("nodes expanded: " + str(expanded))
        print("nodes generated: " + str(generated))
        print("max nodes in memory: " + str(max_nodes))
        print("distance: infinity")
        print("route: none")


def uniform_cost_search(origin, destination, file):
    """

    :param origin: the start destination
    :param destination: the final destination
    :param file: the successor function. input.txt file
    :return: outputs all the information. nodes expanded, generated, max nodes, distance, and route.
    """

    graph = make_graph(file)
    generated = 0
    expanded = 0
    path = []
    visited = []
    max_nodes = 0
    path = {}
    succ = graph.adjacency_list[origin]
    path[origin] = []

    """This is going through the list of successors, one by one. Then, the successors are pushed onto the stack."""
    for location in succ:
        heapq.heappush(graph.priority_queue, (location[1], location))
        generated += 1
        path[origin].append((location[0]))

    visited.append(origin)
    expanded += 1
    max_nodes = len(graph.priority_queue)
    flag = False
    cumm_weight = 0

    while len(graph.priority_queue) != 0:
        """we are popping a tuple, and checking the indices 0 - the destination"""
        current_destination = heapq.heappop(graph.priority_queue)[-1]
        expanded += 1

        if current_destination[0] == destination:
            flag = True
            cumm_weight = current_destination[1]
            break

        succ = graph.adjacency_list[current_destination[0]]

        if current_destination[0] not in visited:
            path[current_destination[0]] = []
            for location in succ:
                path[current_destination[0]].append(location[0])
                cumm_weight = current_destination[1] + location[1]
                heapq.heappush(graph.priority_queue, (cumm_weight, (location[0], cumm_weight)))
                generated += 1
            visited.append((current_destination[0]))

        if len(graph.priority_queue) > max_nodes:
            max_nodes = len(graph.priority_queue)

    if flag:
        print("nodes expanded: " + str(expanded))
        print("nodes generated: " + str(generated))
        print("max nodes in memory: " + str(max_nodes))
        print("distance: " + str(cumm_weight) + " km")
        print(origin + " to " + destination + ": " + str(cumm_weight) + " km")

    else:
        print("nodes expanded: " + str(expanded))
        print("nodes generated: " + str(generated))
        print("max nodes in memory: " + str(max_nodes))
        print("distance: infinity")
        print("route: none")

if __name__ == '__main__':

    graph_file = " "
    origin_city = " "
    destination_city = " "
    heuristic_file = " "

    if len(sys.argv) <= 5:
        graph_file = sys.argv[1]
        origin_city = sys.argv[2]
        destination_city = sys.argv[3]

    if len(sys.argv) == 5:
        heuristic_file = sys.argv[4]
        A_star(origin_city, destination_city, graph_file, heuristic_file)

    if len(sys.argv) == 4:
        uniform_cost_search(origin_city, destination_city, graph_file)
