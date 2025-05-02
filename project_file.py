from queue import PriorityQueue 
from collections import defaultdict
import os
import time


"""
Uses Prims algorithm to find the mst of a graph and writes to output file of the nodes
we traverse in the order of minimum edge weight. 

Args: 
    adj_list for our graph representation 
    represented in the form {node: [edge_length, start_node, end_node, edge_id]} 
    edge length is first in the list because when we use priority queue it takes the first value
    in the list to maintain our min heap

Returns:
    edge_set to represent the edges that we used to minimize the cost
    edje_sum to calculate the total cost of the optimal edge set
"""
def prims_algorithm(adj_list):
    # variables to store our edges and nodes
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
        # pop a node with the min edge weight off the heap 
        popped_node = q.get()

        # extract each variable for easier reading
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
            # remove trailing and leading white space
            parts = line.strip().split()

            # extract relevant variables in the file
            edge_id = int(parts[0])
            start = int(parts[1])
            end = int(parts[2])
            length = float(parts[3])
            
            # add our variables for our nodes in the format of a list of lists 
            edge_representation.append([edge_id, start, end, length])
    
    return edge_representation

"""
Writes data to a specified file.

Args: 
    filename: name of file 
    text: string that will be used to write to a file

Returns:
    None
"""
def write_file(file_name,text):
    # Writing to a file
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

"""
Given the edge representation in the format [edge_id, start node, end node, edge length], it will
create an adjacency list as a dictionary of lists. It will be in the format of 
{node: [edge length, start node, end node, edge length]}

Args:
    edge_representation: list containing node data 

Returns:
    adj_list
"""
def create_adj_list(edge_representation):
    # create a default dict of lists so we can constantly create new key, value pairs
    adj_list = defaultdict(list)

    # loop through every node data in edge_representation
    for line in edge_representation:
        # extract variables from list for readability
        start_node = line[1]
        end_node = line[2]
        edge_length = line[3]
        edge_id = line[0]

        # add data to adjacency list. Add twice to account for an undirected graph
        adj_list[start_node].append((edge_length, start_node, end_node, edge_id)) 
        adj_list[end_node].append((edge_length, end_node, start_node, edge_id)) 

    return adj_list


def main():
    open("output.txt", "w").close()
    edge_representation = read_file('cal.cedge.txt')
    adj_list = create_adj_list(edge_representation)
    start_time = time.time()
    edge_set, edge_sum = prims_algorithm(adj_list)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Prim's Algorithm completed in {duration:.6f} seconds.")
    print(f"Total MST Cost: {edge_sum}")

if __name__ == '__main__':
    main()