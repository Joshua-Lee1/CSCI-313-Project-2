from queue import PriorityQueue 
import os
import time
from Kruskals_Algo import kruskals_algorithm
from Helper_Functions import read_file, write_file, create_adj_list

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
def prims_algorithm(adj_list,output_file_name):
    # variables to store our edges and nodes
    edge_set = set()
    visited = set()
    edge_sum = 0
    solution_str = ""

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
            solution_str += f"{edge_id} {start_node} {end_node} {edge_length}\n"
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
        
    write_file(output_file_name, solution_str)
    return edge_set, edge_sum



def main():
    open("output.txt", "w").close()
    edge_representation = read_file('cal.cedge.txt')
    adj_list = create_adj_list(edge_representation)
    user_input = input("Enter 1 for prim, 2 for Kruskals")
    if user_input == "1":
        start_time = time.time()
        edge_set, edge_sum = prims_algorithm(adj_list,"Prim_Output.txt")
        end_time = time.time()
        duration = end_time - start_time
        print(f"Prim's Algorithm completed in {duration:.6f} seconds.")
    else:
        start_time = time.time()
        edge_sum = kruskals_algorithm(adj_list,edge_representation,"KRUSKAL_ANS.txt")
        end_time = time.time()
        duration = end_time - start_time
        print(f"Kruskal's Algorithm completed in {duration:.6f} seconds.")
    
    print(f"Total MST Cost: {edge_sum}")

if __name__ == '__main__':
    main()