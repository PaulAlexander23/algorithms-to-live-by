
from algorithmstolivebypaulalexander.item import Item
from algorithmstolivebypaulalexander.sorting_problem import sorting_problem, searching_problem
from algorithmstolivebypaulalexander.sorting_algorithms import algorithm, bubble_sort, linear_search

def sorting():
    N = int(input("Enter the number of items: "))
    p = sorting_problem(N)

    # Get user input to select the algorithm
    print("Select an algorithm:")
    print("1. Bubble Sort")
    #print("2. Selection Sort")
    #print("3. Insertion Sort")
    #print("4. Merge Sort")
    #print("5. Quick Sort")
    #print("6. Heap Sort")

    index = input("Enter the number of the algorithm: ")

    a = algorithm()

    if index == "1":
        a = bubble_sort()
    #elif algorithm == "2":
    #    a = selection_sort()

    s = a.solve(p)

    if N != 0:
        for i in range(N):
            print(f"{s[i].name}: {s[i].value}")

def searching():
    N = int(input("Enter the number of items: "))
    T = int(input("Enter the target: "))

    # Get user input to select the algorithm
    print("Select an algorithm:")
    print("1. Linear search")
    print("2. Bubble Sort search")

    index = input("Enter the number of the algorithm: ")

    p = searching_problem(N,T)
    a = linear_search()
    result = a.solve(p)

    if N != 0:
        for i in range(N):
            print(f"{p.items[i].name}: {p.items[i].value}")
    print("Target:", T, "is", "found." if result == 1 else "not found.")


def main():
    print("Sorting and searching")

    # Get user input to select the algorithm
    print("Select a problem:")
    print("1. Sorting")
    print("2. Searching")

    if input("Enter the number of the problem: ") == "1":
        sorting()
    else:
        searching()
    return 0

if __name__ == "__main__":
    main()
