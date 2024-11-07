class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def knapsack(W, items):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = [0] * n
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items[i - 1] = 1
            w -= items[i - 1].weight

    return dp[n][W], selected_items


W = int(input("Enter the Knapsack Capacity: "))
items = []
n = int(input("Enter the Number of Items: "))
for i in range(n):
    weight = int(input(f"Enter Weight of Item {i+1}: "))
    value = int(input(f"Enter Value of Item {i+1}: "))
    items.append(Item(weight, value))

max_value, selected_items = knapsack(W, items)
print("Selected Items:\n", *selected_items)
print("Maximum Profit:", max_value)
