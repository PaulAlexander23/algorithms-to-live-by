
class algorithm:
    def __init__(self):
        pass

    def solve(self, problem):
        pass

class bubble_sort(algorithm):
    def __init__(self):
        pass

    def solve(self, problem):
        # Bubble sort the items

        for i in range(len(problem.items)):
            for j in range(len(problem.items) - 1):
                if problem.items[j].value > problem.items[j + 1].value:
                    problem.items[j], problem.items[j + 1] = problem.items[j + 1], problem.items[j]

        return problem.items

class linear_search(algorithm):
    def __init__(self):
        pass

    def solve(self, problem):

        # Search for the target value

        for i in range(len(problem.items)):
            if problem.items[i].value == problem.target:
                return 1

        return 0

class bubble_sort_search(algorithm):
    def __init__(self):
        pass

    def solve(self, problem):
        # Bubble sort the items

        for i in range(len(problem.items)):
            for j in range(len(problem.items) - 1):
                if problem.items[j].value > problem.items[j + 1].value:
                    problem.items[j], problem.items[j + 1] = problem.items[j + 1], problem.items[j]

        # Search for the target value

        for i in range(len(problem.items)):
            if problem.items[i].value == problem.target:
                return 1

        return 0
