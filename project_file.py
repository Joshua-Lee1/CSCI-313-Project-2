from queue import PriorityQueue 
import os
import time
from Kruskals_Algo import kruskals_algorithm
from Prims_Algo import prims_algorithm
from Helper_Functions import read_file, create_adj_list
import sys


"""
def prompt_file_selection():
    valid_files = ["NA.cedge.txt", "OL.cedge.txt", "SF.cedge.txt", "TG.cedge.txt", "cal.cedge.txt"]
    print("\nAvailable files:")
    for i, file in enumerate(valid_files, 1):
        print(f"  {i}. {file}")
    print("  0. Exit")

    while True:
        user_input = input("\nEnter the number corresponding to the file you'd like to use (0 to exit): ").strip()
        if user_input.isdigit():
            index = int(user_input)
            if index == 0:
                return None
            elif 1 <= index <= len(valid_files):
                return valid_files[index - 1]
        print("Invalid selection. Please try again with a number from the list.")
"""


def main():
    if len(sys.argv) != 4:
        print("Usage: python your_script.py <algorithm_name> <input_file> <output_file> \n The algorithms are 'Prim' and 'Kruskal' ")
        sys.exit(1)
    algo = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

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