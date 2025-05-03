from queue import PriorityQueue 
import os
import time
from Kruskals_Algo import kruskals_algorithm
from Prims_Algo import prims_algorithm
from Helper_Functions import read_file, create_adj_list
import sys



def prompt_algorithm_selection():
    algorithms = ["Prim", "Kruskal"]
    print("\nSelect algorithm:")
    for i, algo in enumerate(algorithms, 1):
        print(f"  {i}. {algo}")

    while True:
        user_input = input("\nEnter the number corresponding to the algorithm you'd like to use: ").strip()
        if user_input.isdigit():
            index = int(user_input)
            if 1 <= index <= len(algorithms):
                return algorithms[index - 1]
        print("Invalid selection. Please try again with a number from the list.")




def main():
    if len(sys.argv) != 3:
        print("Usage: python <your_script.py> <input_file> <output_file> ")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    algo = prompt_algorithm_selection()
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    print(f"\nReading from file: {input_file}\n")
    
    # Clear the output file if it exists
    open(output_file, "w").close()

    edge_representation = read_file(input_file)
    adj_list = create_adj_list(edge_representation)
    if algo == "Prim":
        start_time = time.time()
        edge_set, edge_sum = prims_algorithm(adj_list, output_file)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Prim's Algorithm completed in {duration:.6f} seconds.")
    else:
        start_time = time.time()
        edge_sum = kruskals_algorithm(adj_list,edge_representation, output_file)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Kruskal's Algorithm completed in {duration:.6f} seconds.")
    
    print(f"Total MST Cost: {edge_sum}")
    print(f"Results saved to {output_file}\n")


if __name__ == '__main__':
    main()