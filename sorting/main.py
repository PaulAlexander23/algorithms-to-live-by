import sys
import os

# Add the subfolder to the system path
sys.path.append(os.path.dirname(os.path.relpath("../")))

from sorting.item import item
from sorting.problem import sorting_problem
from sorting.algorithm import algorithm, bubble_sort

def main():
    print("Sorting")

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

    if N == 0:
        return 0

    for i in range(N):
        print(f"{s[i].name}: {s[i].value}")

    return 0

if __name__ == "__main__":
    main()
