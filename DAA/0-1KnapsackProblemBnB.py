class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_branch_and_bound(capacity, items):
    def bound(i, weight, value):
        if weight > capacity:
            return 0
        bound_value = value
        j = i
        total_weight = weight
        while j < n and total_weight + items[j].weight <= capacity:
            total_weight += items[j].weight
            bound_value += items[j].value
            j += 1
        if j < n:
            bound_value += (capacity - total_weight) * (items[j].value / items[j].weight)
        return bound_value

    def knapsack_recursive(i, weight, value, selected):
        nonlocal max_value, best_selection
        if weight <= capacity and value > max_value:
            max_value = value
            best_selection = selected[:]
        if i < n:
            if weight + items[i].weight <= capacity:
                selected[i] = 1
                knapsack_recursive(i + 1, weight + items[i].weight, value + items[i].value, selected)
                selected[i] = 0
            if bound(i + 1, weight, value) > max_value:
                knapsack_recursive(i + 1, weight, value, selected)

    n = len(items)
    max_value = 0
    best_selection = [0] * n
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    knapsack_recursive(0, 0, 0, [0] * n)
    return max_value, best_selection

W = int(input("Enter the Knapsack Capacity: "))
items = []
n = int(input("Enter the Number of Items: "))
for i in range(n):
    weight = int(input(f"Enter Weight of Item {i+1}: "))
    value = int(input(f"Enter Value of Item {i+1}: "))
    items.append(Item(weight, value))

max_value, selected_items = knapsack_branch_and_bound(W, items)
print("Selected Items:\n", selected_items)
print("Maximum Profit:", max_value)
