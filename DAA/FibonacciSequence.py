class Fibonacci:
    def recursive_fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.recursive_fibonacci(n - 1) + self.recursive_fibonacci(n - 2)

    def non_recursive_fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]

        first, second = 0, 1
        sequence = [first, second]

        for _ in range(n - 2):
            third = first + second
            sequence.append(third)
            first, second = second, third

        return sequence

def menu():
    fib = Fibonacci()
    while True:
        print("\n*********MENU*********")
        print("1. Recursive Fibonacci")
        print("2. Iterative Fibonacci")
        print("3. Exit")

        choice = input("Enter Your Choice:")

        if choice == "1":
            n = int(input("Enter the Number of Terms for Recursive Fibonacci:"))
            print("Recursive Fibonacci Sequence:")
            for i in range(n):
                print(fib.recursive_fibonacci(i), end=" ")
            print()

        elif choice == "2":
            n = int(input("Enter the Number of Terms for Iterative Fibonacci:"))
            print("Iterative Fibonacci Sequence:")
            result = fib.non_recursive_fibonacci(n)
            print(*result)

        elif choice == "3":
            print("!!THANK YOU!!")
            break

        else:
            print("Invalid Input, Please Try Again")


if __name__ == "__main__":
    menu()