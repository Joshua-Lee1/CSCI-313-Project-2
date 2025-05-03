# CSCI-313-Project-2 City Connection Project

Provides an interface to use two different algorithms (kruskal's or Prims) on a variety of different data sets
according to the user's choice. The algorithms will return the MST of the given graph and write output of the 
edges and nodes taken to a separate file. 

## Overview

This project is designed for CSCI-313 to demonstrate understanding of graph algorithms. It simulates connecting nodes in the most cost-effective way using MST techniques. Users can choose which algorithm to run and on which dataset, enabling easy comparison and analysis.


## Features

- Run **Kruskal's** or **Prim's** algorithm on user-specified datasets
- Handles different input graphs
- Outputs MST edge list and total time used for either algorithm
- Command-line interface for user interaction


## Algorithms Used

- **Kruskal's Algorithm**: Greedy approach using Union-Find to prevent cycles.
- **Prim's Algorithm**: Greedy approach using a priority queue to grow the MST.

## How to run
Run the program from the terminal:
python project_file.py <input_file> <output_file>
