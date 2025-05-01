from queue import PriorityQueue 
from collections import defaultdict
import os


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
        edge_id = popped_node[3]
        start_node = popped_node[1]
        end_node = popped_node[2]
        edge_length = popped_node[0]
        ## process it if it has not been visited yet
        if popped_node[2] not in visited:
            write_file("output.txt", f"{edge_id} {start_node} {end_node} {edge_length}")
            ## mark as visited
            visited.add(end_node)
            ## add the minimum edge to the edge set
            edge_set.add(edge_id)
            ## calculate the edge sum
            edge_sum += edge_length

            ## Check the neighbors of the node we are processing and add its edges to the priority queue
            for neighbor in adj_list[end_node]:
                if neighbor[2] not in visited:
                    q.put(neighbor)

    return edge_set, edge_sum


"""
Reads file in the format of edge id, start node, end node, edge distance 

Args: 
    name of file containing graph connections

Returns:
    adjacency list of graph which contains the node as the key, and a list of
    [edge, start node, end node, edge_id] or [edge, end node, start node, edge_id] to account for an 
    undirected graph.
"""
def read_file(file_name):
    ## keep edge representation in the form of a list of lists so it is easier for us to process
    edge_representation = []
    ## open the file and process each line
    with open("cal.cedge.txt", "r") as file:
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
        adj_list[start].append((edge, start, end, edge_id)) 
        adj_list[end].append((edge, end, start, edge_id)) 

    return adj_list

def write_file(file_name,text):
    # Writing to a file
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    open("output.txt", "w").close()
    adj_list = read_file('cal.cedge.txt')
    prims_algorithm(adj_list)


if __name__ == '__main__':
    main()