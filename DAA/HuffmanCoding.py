import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printnodes(node, val=""):
    newval = val + str(node.huff)

    if node.left:
        printnodes(node.left, newval)
    if node.right:
        printnodes(node.right, newval)

    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol, newval))


if __name__ == "__main__":
    num_elements = int(input("Enter the Number of Elements: "))

    chars = []
    freq = []
    for i in range(num_elements):
        symbol = input(f"\nEnter Character:")
        chars.append(symbol)
        frequency = int(input(f"Enter Frequency of '{symbol}': "))
        freq.append(frequency)

    print("\nHuffman Codes Are:")

    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, node(freq[i], chars[i]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)

    printnodes(nodes[0])