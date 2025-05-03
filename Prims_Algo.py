from Helper_Functions import write_file

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        # Swap root with last and heapify down
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


"""
Uses Prims algorithm to find the mst of a graph and writes to output file of the nodes
we traverse in the order of minimum edge weight. 

Args: 
    adj_list for our graph representation 
    represented in the form {node: [edge_length, start_node, end_node, edge_id]} 
    edge length is first in the list because when we use priority queue it takes the first value
    in the list to maintain our min heap
    output file for where the results will be saved

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
    q = MinHeap() 
    node, neighbors = next(iter(adj_list.items()))
    for neighbor in neighbors:
        q.push(neighbor)
    visited.add(node)

    ## check every edge
    while not q.is_empty():
        # pop a node with the min edge weight off the heap 
        popped_node = q.pop()

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