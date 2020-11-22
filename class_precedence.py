from operator import add
from functools import reduce

'''
Representation of a graph using adjacency lists
'''
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Shorthand method for returning the elements in adjacency list of the graph
    def items(self):
        return self.adjacency_list.items()

    # Adds an ako (a kind of) or is-a relationship to the graph as a vertex
    def ako(self, subclass, superclass):
        if subclass not in self.adjacency_list:
            self.adjacency_list[subclass] = []

        if superclass not in self.adjacency_list:
            self.adjacency_list[superclass] = []

        self.adjacency_list[subclass].append(superclass)

    # Create fish hook pairs as a dict where keys are nodes and values are pairs
    def fish_hook_pairs(self):
        result = {}
        for key, values in self.items():
            pairs = []
            if len(values) == 0:
                pairs.append((key, "*"))
            else:
                left = key
                for value in values:
                    right = value
                    pairs.append((left, right))
                    left = right
            result[key] = pairs
        return result

    def class_precedence_list(self):
        # To compute an instance's class precedence list,
        precedence_list = []

        # Create fish-hook pairs
        fhpairs = self.fish_hook_pairs()
        classes_list = list(fhpairs.keys())
        pairs_list = reduce(add, list(fhpairs.values()))

        # Until all the fish-hook pairs are eliminated
        while(len(pairs_list) > 0):

            # Find the exposed classes
            exposed_classes = classes_list[:]
            for pair in pairs_list:
                # If a class appears on the right side of a pair, it is not exposed
                if pair[1] in exposed_classes:
                    exposed_classes.remove(pair[1])

            # Select the exposed class that is a direct superclass of the
            # lowest-precedence class on the emerging class-precedence list
            selected_class = exposed_classes[0]
            if len(exposed_classes) > 1:
                found = False
                # Iterate precedence-list in reverse order
                for class_name in reversed(precedence_list):
                    # For each tied class
                    for exposed_class in exposed_classes:
                        # Check if tied class is a direct superclass of the current item in precedence list
                        for tuple in fhpairs[class_name]:
                            if tuple[1] == exposed_class:
                                selected_class = exposed_class
                                found = True
                                break
                    if found:
                        break
            
            # Add the selected class to the emerging class-precedence list
            precedence_list.append(selected_class)

            # Remove the selected class from classes list
            classes_list = [class_name for class_name in classes_list if class_name != selected_class]

            # Strike all fish-hook pairs that contain the newly added class
            pairs_list = [pair for pair in pairs_list if pair[0] != selected_class]

        return precedence_list

def main():

    # Example from book
    obj = Graph()
    obj.ako("Crazy", "Professors")
    obj.ako("Crazy", "Hackers")
    obj.ako("Professors", "Eccentrics")
    obj.ako("Professors", "Teachers")
    obj.ako("Hackers", "Eccentrics")
    obj.ako("Hackers", "Programmers")
    obj.ako("Eccentrics", "Dwarfs")
    obj.ako("Teachers", "Dwarfs")
    obj.ako("Programmers", "Dwarfs")
    obj.ako("Dwarfs", "Everything")
    print(obj.class_precedence_list())

    # Part 1

    # Part 2

    # Part 3


if __name__ == "__main__":
    main()

