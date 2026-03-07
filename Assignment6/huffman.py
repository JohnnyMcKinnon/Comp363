from __future__ import annotations
import heapq
from pympler import asizeof


class Node:
    def __init__(self, symbol: str | None, frequency: int):
        # Each node stores:
        # - symbol (leaf/no leaf)
        # - frequency
        # - 2 pointers; left and right children nodes
        self.__frequency = frequency
        self.__symbol = symbol
        self.__left = None
        self.__right = None

    # Allows nodes to be compared inside the heap
    # Node with smaller frequency=higher priority
    def __lt__(self, other):
        return self.__frequency < other.get_frequency()

    # set left child
    def set_left(self, node):
        self.__left = node

    # set right child
    def set_right(self, node):
        self.__right = node

    # Get left child
    def get_left(self):
        return self.__left

    # Get right child
    def get_right(self):
        return self.__right

    # Return symbol from node
    def get_symbol(self):
        return self.__symbol

    # Return frequency from same node
    def get_frequency(self):
        return self.__frequency

    # node=leaf if it has 0 children
    def is_leaf(self):
        return self.__left is None and self.__right is None


class Huffman:

    def __init__(self, message: str):
        #stores input
        self.message = message
        
        # Will eventually point to root of Huffman tree
        self.root = None
        
        # Maps characters to their Huffman codes
        self.codes = {}


    #Count character frequencies
    def build_frequencies(self):
        freq = {}
        
        # Count (frequency) how many times each character appears
        for ch in self.message:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                
        return freq

    # Step 2: Build Huffman tree
    def build_tree(self):
        freq = self.build_frequencies()
        heap = []

        # Convert each (symbol, frequency) pair into a leaf node
        # and push to a min-heap
        for symbol in freq:
            heapq.heappush(heap, Node(symbol, freq[symbol]))

        # Keep combining two smallest nodes until only one node remains (-->root)
        while len(heap) > 1:
            node1 = heapq.heappop(heap)  # smallest frequency
            node2 = heapq.heappop(heap)  # second smallest

            # Create new internal node
            merged = Node(None, node1.get_frequency() + node2.get_frequency())

            # Attach both nodes as children
            merged.set_left(node1)
            merged.set_right(node2)

            # Push merged node back into heap
            heapq.heappush(heap, merged)

        # Final remaining node is the root of the Huffman tree
        self.root = heapq.heappop(heap)


    # Step 3: Generate Huffman codes
    def generate_codes(self):

        # Recursive function to traverse tree
        def traverse(node, current_code):
            if node is None:
                return

            # If leaf, assign given Huffman code
            if node.is_leaf():
                self.codes[node.get_symbol()] = current_code
                return

            # Go left -> add "0"
            traverse(node.get_left(), current_code + "0")

            # Go right -> add "1"
            traverse(node.get_right(), current_code + "1")

        # Start traversal from root
        traverse(self.root, "")

    # Encode message
    def encode(self):
        # Build tree and generate codes first
        self.build_tree()
        self.generate_codes()

        encoded = ""

        # Replace each character with Huffman code
        for ch in self.message:
            encoded += self.codes[ch]

        return encoded

    # Decode message
    def decode(self, encoded_message):
        decoded = ""
        current = self.root  # Start at root

        # Read encoded message bit by bit
        for bit in encoded_message:
            # Move left or right depending on bit
            if bit == "0":
                current = current.get_left()
            else:
                current = current.get_right()

            # If leaf--> found a character
            if current.is_leaf():
                decoded += current.get_symbol()
                current = self.root  # Reset back to root

        return decoded

    # Print compression statistics
    def report(self, encoded_message):
        ascii_bits = len(self.message) * 8   # ASCII (8 bits per character)
        huffman_bits = len(encoded_message)  # Length of encoded bit string

        # Measure memory needed to store Huffman tree
        tree_size_bytes = asizeof.asizeof(self.root)
        tree_size_bits = tree_size_bytes * 8

        print("\n--- Compression Results ---")
        print("ASCII size:", ascii_bits, "bits")
        print("Huffman size:", huffman_bits, "bits")
        print("Bits saved (without tree):", ascii_bits - huffman_bits)
        print("Tree size:", tree_size_bits, "bits")
        print("Net gain/loss including tree:",
              ascii_bits - (huffman_bits + tree_size_bits), "bits")


# Testing
if __name__ == "__main__":

    message = "HELLO WORLD"

    h = Huffman(message)

    encoded = h.encode()
    decoded = h.decode(encoded)

    print("Original:", message)
    print("Encoded :", encoded)
    print("Decoded :", decoded)

    h.report(encoded)