'''
Representation of a graph using adjacency lists
'''
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def items(self):
        return self.adjacency_list.items()

    def ako(self, subclass, superclass):
        if subclass not in self.adjacency_list:
            self.adjacency_list[subclass] = []

        if superclass not in self.adjacency_list:
            self.adjacency_list[superclass] = []

        self.adjacency_list[subclass].append(superclass)

    def fish_hook_pairs(self):
        result = {}
        for key, values in self.items():
            pairs = []
            if len(values) == 0:
                pairs.append((key, "Everything"))
            else:
                left = key
                for value in values:
                    right = value
                    pairs.append((left, right))
                    left = right
            result[key] = pairs
            result["Everything"] = [("Everything")]
        return result.items()

def main():
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
    pairs = obj.fish_hook_pairs()
    for pair, value in pairs:
        print(pair, value)

if __name__ == "__main__":
    main()

