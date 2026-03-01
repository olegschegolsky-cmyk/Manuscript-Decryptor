# Manuscript-Decryptor
A software framework for implementing a highly efficient algorithm to search for a set of words within a 2D character matrix. The solution is based on the Trie (prefix tree) data structure and Depth-First Search (DFS) algorithm, featuring memory optimization via in-place state mutation of the matrix

# Manuscript Decryptor: 2D Grid Word Search Engine

## Project Overview
This repository provides an architectural template for solving the problem of finding a specified dictionary of terms within a 2D N x M character grid. The project requires the implementation of an optimized graph traversal algorithm that meets the performance standards of high-load systems.

## Technical Requirements & Traversal Rules
1. **Movement Directions:** Transitions between nodes (matrix cells) are allowed in 8 directions (horizontally, vertically, and diagonally).
2. **Node Uniqueness:** Each matrix cell can be used at most once during the formation of a single word.
3. **Memory Optimization:** The use of auxiliary matrices or data structures for tracking visited cells (e.g., `visited` sets) is strictly prohibited. State tracking must be achieved through in-place mutation of the original matrix.
4. **Runtime Optimization:** The algorithm must support dynamic pruning of the prefix tree branches (Dynamic Trie Pruning). Upon successfully finding a word, the corresponding tree node must be deactivated to prevent redundant traversal.

## Architecture
The template consists of three core components:

* `TrieNode`: A class representing an individual node of the prefix tree.
* `Trie`: A data structure for storing and optimizing the search of dictionary prefixes.
* `ManuscriptDecryptor`: The main controller class containing the `find_words` method, responsible for initializing the tree and executing the DFS traversal of the matrix.

## Usage

The current state of the codebase is a skeleton framework. Full operational capability requires the implementation of the internal logic within the `TrieNode`, `Trie`, and `ManuscriptDecryptor` classes.
