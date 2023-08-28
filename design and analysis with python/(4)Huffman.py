import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char, self.freq, self.left, self.right = char, freq, None, None

    def __lt__(self, other):
        return self.freq < other.freq if isinstance(other, HuffmanNode) else NotImplemented

def build_huffman_tree(chars, freqs):
    heap = [HuffmanNode(c, f) for c, f in zip(chars, freqs)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        combined = HuffmanNode(None, heap[0].freq + heap[1].freq)
        combined.left, combined.right = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, combined)
    
    return heapq.heappop(heap)

def build_huffman_codes(root, code='', codes={}):
    if root:
        if root.char:
            codes[root.char] = code
        build_huffman_codes(root.left, code + '0', codes)
        build_huffman_codes(root.right, code + '1', codes)

def encode_decode_string(encoded, root):
    decoded, current = '', root
    for bit in encoded:
        current = current.left if bit == '0' else current.right
        if current.char:
            decoded += current.char
            current = root
    return decoded

def get_input(count, data_type):
    return [data_type(input(f"Enter {'char' if data_type == str else 'prob'} {i+1}: ")) for i in range(count)]

def main():
    n = int(input("Enter number of chars: "))
    chars = get_input(n, str)
    freqs = get_input(n, float)
    tree = build_huffman_tree(chars, freqs)
    codes = {}
    build_huffman_codes(tree, '', codes)

    string = input("Enter a string: ")
    encoded = ''.join(codes[char] for char in string)

    print("Huffman Codes:")
    for char, code in codes.items():
        print(char, ":", code)

    if input("Decode string? (Y/N): ").lower() == 'y':
        binary = encoded if input("Binary? (Y/N): ").lower() == 'y' else input("Enter binary: ")
        decoded = encode_decode_string(binary, tree)
        print("Decoded string:", decoded)
    else:
        print("Decoding skipped.")

if __name__ == "__main__":
    main()
