inf = float('inf')
start = "A"
stop = "D"

graph = {}

graph['A'] = {}
graph['A']['A'] = 0
graph['A']['B'] = 1
graph['A']['C'] = 3

graph['B'] = {}
graph['B']['B'] = 10
graph['B']['C'] = 1
graph['B']['D'] = 5

graph['C'] = {}
graph['C']['C'] = 1
graph['C']['D'] = 3


graph['D'] = {}
graph['D']['D'] = 0

# graph['A'] = {}
# graph['A']['A'] = 0
# graph['A']['B'] = 20
# graph['A']['F'] = 20
# graph['A']['E'] = 20

# graph['B'] = {}
# graph['B']['B'] = 0
# graph['B']['C'] = 25

# graph['C'] = {}
# graph['C']['C'] = 0
# graph['C']['D'] = 10
# graph['C']['F'] = 10

# graph['D'] = {}
# graph['D']['D'] = 0
# graph['D']['I'] = 10

# graph['E'] = {}
# graph['E']['E'] = 20
# graph['E']['F'] = 10
# graph['E']['I'] = 30

# graph['F'] = {}
# graph['F']['F'] = 10
# graph['F']['G'] = 10

# graph['G'] = {}
# graph['G']['G'] = 5
# graph['G']['H'] = 10

# graph['H'] = {}
# graph['H']['H'] = 5
# graph['H']['I'] = 10

# graph['I'] = {}
# graph['I']['I'] = 0


# iterate over every node and set the cost to get to that node to infinity
# until you've gone to that node it costs infinite amount
# identify a dictionary that shows parents how to get to a node
costs = {}
parents = {}
for node in graph:
    costs[node] = inf
    parents[node] = {}
# set the cost of starting node to be cheapest node of 0
costs[start] = 0

# function to find the cheapest node
def find_cheapest_node(costs, not_checked):
    print(f"Cheapeset Node Method: (costs: {costs}, not_checked: {not_checked})")
    cheapest_node = None
    lowest_cost = inf
    for node in not_checked:
        print(f"**{node}: {costs[node] + graph[node][node]}")
        if costs[node] <= lowest_cost:
            lowest_cost = costs[node]
            cheapest_node = node
    return cheapest_node



# Search shortest path
if __name__ == "__main__":
    # these are nodes we have not checked/visited yet
    not_checked = [node for node in costs]

    # find the cheapest node using the method
    node = find_cheapest_node(costs, not_checked)

    # iterate over nodes that have not been checked
    while not_checked:
        # print nodes that have not been checked
        print()
        print(f"Not Checked: {not_checked}")
        print(f"Current Node = {node}")

        # Add Self loop node cost
        print(f"Node[{node}] Self Loop Cost = {graph[node][node]}")

        # grab cost of the current node
        cost = costs[node] + graph[node][node]
        print(f"{node} Node Total Cost = {cost}")

        # grab cost of node next in the graph aka child node
        child_cost = graph[node]
        # print(f"Child Node Costs = {child_cost}")
        

        # iterate over the child nodes and compare the cost of the current node
        for c in child_cost:
            # print(f"Child Node[{c}]: {costs[c]}")
            # if the cost of the child path we are currently looking at is less than the cost we have currently,
            if costs[c] > cost + child_cost[c]:
                # then update the current cost to that of the shorter child path
                costs[c] = cost + child_cost[c]
                # print(f"Cost[{c}]: {costs[c]}")
                # also update the parent node so that we can backtrack and find the cheapest path
                parents[c] = node
                # print(f"Parents[{c}]: {parents[c]}")
        
        # pop that node out of the list
        not_checked.pop(not_checked.index(node))
        # continue finding the next cheapest node
        # if there are no more cheap nodes that the while loop will stop executing
        node = find_cheapest_node(costs, not_checked)
    
    
    print(f"Costs: {costs}")
    print(f"The cost to go from {start} to {stop} is {costs[stop]}")

    # print of final path
    if costs[stop] < inf:
        path = [stop]
        i = 0
        while start not in path:
            path.append(parents[path[i]])
            i += 1
        
        print(f"The shorest path is {path[::-1]}")
    else:
        print(f"A path could not be found")




