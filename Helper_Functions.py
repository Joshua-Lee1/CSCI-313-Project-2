from collections import defaultdict
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
    with open(file_name, "r") as file:
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
        with open(file_name, "w") as file:
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