'''
Representation of a graph using adjacency lists
'''
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def ako(self, subclass, superclass):
        if subclass not in self.adjacency_list:
            self.adjacency_list[subclass] = []

        if superclass not in self.adjacency_list:
            self.adjacency_list[superclass] = []

        self.adjacency_list[subclass].append(superclass)


def main():
    obj = Graph()
    obj.ako("BMW", "Car")
    obj.ako("Car", "Vehicle")
    obj.ako("BMW", "Fast")
    print(obj.adjacency_list)

if __name__ == "__main__":
    main()

