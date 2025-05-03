from Helper_Functions import write_file

"""
Uses Kruskals Algorithm to create an MST of a graph and writes the output to KRUSKAL_ANS.txt

Args: 
    adj_list for our graph representation 
    represented in the form {node: [edge_length, start_node, end_node, edge_id]} 
    edge length is first in the list because we use a priority queue so we can quickly check

Returns:

    edge_sum to calculate the total cost of the optimal edge set
"""

def kruskals_algorithm(adj_list, edge_representation,output_file_name):
    # disjoint Set to track our progress on Kruskals Algorithm
    edge_sum = 0
    total_verts = len(adj_list.keys())
    disjoint_set = disjointSet(total_verts) #will return the number of nodes and create a disjoint set that long.
    solution = ""

    #using Kruskal makes it far faster to just send it with the edges as read in
    edge_representation.sort(key=getWeight)
    index = 0
    edge_count = 0
    while edge_count < total_verts - 1 and index < len(edge_representation):
        current_edge = edge_representation[index]
        #extract each variable for easier reading
        edge_id = current_edge[0]
        start_node = current_edge[1]
        end_node = current_edge[2]
        edge_length = current_edge[3]

        #try to union the verts from the edge
        if disjoint_set.union(start_node,end_node):
            total_verts -= 1
            edge_sum += edge_length
            solution += f"{edge_id} {start_node} {end_node} {edge_length}\n"
        index += 1

    # This section write the answer to KRUSKAL_ANS.txt
    write_file(output_file_name,solution)
    return edge_sum

#adopted from geeksforgeeks guide to Kruskal with changed variable names and comments
class disjointSet:
    def __init__(self,num_verts):
        self.whole = list(range(num_verts)) # We can use each index as the node and the value as the parent
        self.sizes = [1 for x in range(num_verts)] #index represents the vertex, number represents the size of the set it is apart of

    def find(self,vert):
        if self.whole[vert] != vert: # If we do not find the vertex in the right spot, we set the index to the value of the parent node by recursively calling find.
            self.whole[vert] = self.find(self.whole[vert]) 
        return self.whole[vert]

    def union(self,vert1,vert2): #returns True on success, False on failure
        loc1 = self.find(vert1)
        loc2 = self.find(vert2)
        if loc1 != loc2:
            if self.sizes[loc1] < self.sizes[loc2]:
                self.whole[loc1] = loc2
            else:
                self.whole[loc2] = loc1
            new_size = self.sizes[loc1] + self.sizes[loc2]
            self.sizes[loc1] = new_size
            self.sizes[loc2] = new_size
            return True
        return False

def getWeight(entry):
    return entry[3]

