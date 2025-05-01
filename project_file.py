from queue import PriorityQueue 
from collections import defaultdict


"""
Uses Prims algorithm to find the mst of a graph.

Args: 
    adj_list for our graph representation

Returns:
    edge_set to represent the edges that we used to minimize the cost
    edje_sum to calculate the total cost of the optimal edge set
"""
def prims_algorithm(adj_list):
    edge_set = set()
    visited = set()
    edge_sum = 0

    ## initialize our start with the first node and its neighbors
    ## priority queue will contain edges
    q = PriorityQueue() 
    node, neighbors = next(iter(adj_list.items()))
    for neighbor in neighbors:
        q.put(neighbor)
    visited.add(node)

    ## check every edge
    while not q.empty():
        popped_node = q.get()
        ## process it if it has not been visited yet
        if popped_node[1] not in visited:
            ## mark as visited
            visited.add(popped_node[1])
            ## add the minimum edge to the edge set
            edge_set.add(popped_node[2])
            ## calculate the edge sum
            edge_sum += popped_node[0]

            ## Check the neighbors of the node we are processing and add its edges to the priority queue
            for neighbor in adj_list[popped_node[1]]:
                if neighbor[1] not in visited:
                    q.put(neighbor)

    return edge_set, edge_sum


"""
Reads file in the format of edge id, start node, end node, edge distance 

Args: 
    name of file containing graph connections

Returns:
    adjacency list of graph which contains the node as the key, and a list of
    [edge, end node, edge_id] or [edge, start node, edge_id] to account for an 
    undirected graph.
"""
def read_file(file_name):
    ## keep edge representation in the form of a list of lists so it is easier for us to process
    edge_representation = []
    ## open the file and process each line
    with open("/content/cal.cedge.txt", "r") as file:
        for line in file:
            # skip comments and blank lines
            if line.startswith("#") or not line.strip():
                continue  
            parts = line.strip().split()
            edge_id = int(parts[0])
            start = int(parts[1])
            end = int(parts[2])
            length = float(parts[3])
            edge_representation.append([edge_id, start, end, length])

    adj_list = defaultdict(list)

    for line in edge_representation:
        start = line[1]
        end = line[2]
        edge = line[3]
        edge_id = line[0]
        adj_list[start].append((edge, end, edge_id)) 
        adj_list[end].append((edge, start, edge_id)) 

    return adj_list

## test