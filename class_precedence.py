part_1_graph = {
    "ifstream" : ["istream"],
    "istream" : ["ios"],
    "fstream" : ["iostream"],
    "iostream" : ["istream", "ostream"],
    "ostream" : ["ios"],
    "ofstream" : ["ostream", "ios"],
    "ios" : ["Everything"],
    "Everything" : []
}

part_2_graph = {
    "Consultant Manager" : ["Consultant", "Manager"],
    "Consultant" : ["Temporary Employee"],
    "Temporary Employee" : ["Employee"],
    "Manager" : ["Employee"],
    "Director" : ["Manager"],
    "Permanent Manager" : ["Manager", "Permanent Employee"],
    "Permanent Employee" : ["Employee"],
    "Employee" : ["Everything"],
    "Everything" : []
}

part_3_graph = {
    "Crazy" : ["Professors", "Hackers"],
    "Professors" : ["Eccentrics", "Teachers"],
    "Hackers" : ["Eccentrics", "Programmers"],
    "Eccentrics" : ["Dwarfs"],
    "Teachers" : ["Dwarfs"],
    "Programmers" : ["Dwarfs"],
    "Dwarfs" : ["Everything"],
    "Everything" : [],
    "Jacque" : ["Weightlifters", "Shotputters", "Athletes"],
    "Weightlifters" : ["Athletes", "Endomorphs"],
    "Shotputters" : ["Athletes", "Endomorphs"],
    "Athletes" : ["Dwarfs"],
    "Endomorphs" : ["Dwarfs"]
}

def class_precedence_lists(graph, single_stepping):
    precedence_lists = []

    if single_stepping:
        print("=== Searching for entry nodes ===")

    exposed_classes = list(graph.keys())
    for key, values in graph.items():
        for parent in values:
            if parent in exposed_classes:
                exposed_classes.remove(parent)

    if single_stepping:
        print("=== Entry nodes are {} ===\n".format(exposed_classes))
    
    for exposed_class in exposed_classes:

        if single_stepping:
            print("=== Computing class precedence list for {} ===".format(exposed_class))

        precedence_lists.append(class_precedence_list(exposed_class, graph, single_stepping))        

    return precedence_lists

def class_precedence_list(start_node, graph, single_stepping):
    # To compute an instance's class-precedence list

    precedence_list = []
    fhpairs = {} 

    if single_stepping:
        print("=== Computing fish hook pairs for {} ===".format(start_node))

    # Create fish-hook pairs
    fish_hooks(start_node, graph, fhpairs)

    classes_list = list(fhpairs.keys())

    # Until all the fish-hook pairs are eliminated:
    while no_of_pairs(fhpairs) > 0:

        if single_stepping:
            print("=== Searching for exposed classes ===")

        # Find the exposed classes
        exposed_classes = find_exposed_classes(classes_list, fhpairs)

        if single_stepping:
            print("=== Exposed classes are {} ===".format(exposed_classes))
            print("=== Selecting next exposed classes ===")

        # Select the exposed class that is a direct superclass of the lowest-precedence class on the emerging class-precedence list
        next_exposed = next_exposed_class(exposed_classes, precedence_list, graph)

        if single_stepping:
            print("=== Next exposed class is {} ===".format(next_exposed))
            print("=== Adding {} to precedence list ===".format(next_exposed))

        # Add the selected class to the emerging class-precedence list
        precedence_list.append(next_exposed)
        classes_list.remove(next_exposed)        

        if single_stepping:
            print("=== Striking fish hook pairs containing {} ===\n".format(next_exposed))
        
        # Strike all fish-hook pairs that contain the newly added class
        strike_fish_hook_pairs(next_exposed, fhpairs)

    if single_stepping:
        print("=== No fish hook pair left ===")
        print("=== Finished calculating class precedence list of {} ===\n".format(start_node))

    return precedence_list

def no_of_pairs(pairs_dict):
    count = 0
    for pairs in pairs_dict.values():
        count += len(pairs)
    return count

def find_exposed_classes(classes_list, fhpairs):
    exposed_classes = classes_list[:]
    for pairs in fhpairs.values():
        for pair in pairs:
            if pair[1] in exposed_classes:
                exposed_classes.remove(pair[1])
    return exposed_classes

def next_exposed_class(exposed_classes, precedence_list, graph):
    if len(exposed_classes) < 1:
        return None
    elif len(exposed_classes) == 1:
        return exposed_classes[0]
    else:
        # Iterate precedence-list in reverse order
        for class_name in reversed(precedence_list):
            # For each tied class
            for exposed_class in exposed_classes:
                # Check if tied class is a direct superclass of the current item in precedence list
                if exposed_class in graph[class_name]:
                    return exposed_class

def strike_fish_hook_pairs(selected_class, fhpairs):
    for key, values in fhpairs.items():
        for pair in values:
            if pair[0] == selected_class:
                fhpairs[key].remove(pair)

def fish_hooks(start_node, graph, pairs):
    if start_node not in graph:
        print("Error")
        return
    pairs[start_node] = []
    left = start_node
    parents = graph[start_node]
    for parent in parents:
        right = parent
        pairs[start_node].append( (left, right) )
        left = right

    for parent in parents:
        # new_pairs = [pair for pair in fish_hooks(parent, graph) if pair not in pairs]
        # pairs = pairs + new_pairs
        fish_hooks(parent, graph, pairs)
    return pairs

def main():
    choice = input("Do you want single stepping? (y/n)") in ["y", "Y", "yes", "Yes", "YES"]
    # Part 1
    print("Solution for part 1:")
    part_1_answer = class_precedence_lists(part_1_graph, choice)
    for answer in part_1_answer:
        print("\nPrecedence list for", answer[0])
        print(answer)

    # Part 2
    input("Press Enter to continue")
    print("Solution for part 2:")
    part_2_answer = class_precedence_lists(part_2_graph, choice)
    for answer in part_2_answer:
        print("\nPrecedence list for", answer[0])
        print(answer)

    # Part 3
    input("Press Enter to continue")
    print("Solution for part 3:")
    part_3_answer = class_precedence_lists(part_3_graph, choice)
    for answer in part_3_answer:
        print("\nPrecedence list for", answer[0])
        print(answer)

if __name__ == "__main__":
    main()



