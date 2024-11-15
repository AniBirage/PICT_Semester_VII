import random


class QuickSort:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i < high and arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quick_sort_deterministic(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quick_sort_deterministic(arr, low, p)
            self.quick_sort_deterministic(arr, p + 1, high)

    def quick_sort_randomized(self, arr, low, high):
        if low < high:
            random_index = random.randint(low, high - 1)
            arr[low], arr[random_index] = arr[random_index], arr[low]
            p = self.partition(arr, low, high)
            self.quick_sort_randomized(arr, low, p)
            self.quick_sort_randomized(arr, p + 1, high)


def menu():
    q_sort = QuickSort()

    while True:
        print("\n*********MENU*********")
        print("1. Deterministic QuickSort")
        print("2. Randomized QuickSort")
        print("3. Exit")
        choice = input("Enter Your Choice:")

        if choice == "1":
            n = int(input("Enter the Number of Elements:"))
            arr = []
            print("Enter the Elements:")
            for _ in range(n):
                element = int(input())
                arr.append(element)
            q_sort.quick_sort_deterministic(arr, 0, len(arr) - 1)
            print("Sorted Array (Deterministic):", *arr)

        elif choice == "2":
            n = int(input("Enter the Number of Elements:"))
            arr = []
            print("Enter the Elements:")
            for _ in range(n):
                element = int(input())
                arr.append(element)
            q_sort.quick_sort_randomized(arr, 0, len(arr) - 1)
            print("Sorted Array (Randomized):", *arr)

        elif choice == "3":
            print("!!THANK YOU!!")
            break

        else:
            print("Invalid Input, Please Try Again")


if __name__ == "__main__":
    menu()