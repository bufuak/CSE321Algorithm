# Classic depth first search for python dictionary data structure Work time is O(departments+roads)
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            neighbours = list(graph[vertex])
            index = len(neighbours)-1
            while neighbours:
                stack.append(neighbours[index])
                neighbours.pop()
                index -= 1
    return visited


# This function finds minimum cost of repairing GTU. Total work time is O(m+n) because of dfs work time.
# If we cover all the department in once this functions work time will be O(m+n) but if our map has 3 separate paths
# then our work time will be O(m1+m2+m3+n1+n2+n3) where m=m1+m2+m3 and n=n1+n2+n3 so work time will be O(n+m)
def findMinimumCostToLabifyGTU(lab_cost,  road_cost, map_of_gtu):
    if lab_cost <= road_cost:                                       # If lab_cost is lesser than road_cost
        return lab_cost*len(map_of_gtu)                             # then min cost is #departments*lab_cost

    departments = list(range(1,len(map_of_gtu)+1))                  # Getting department list
    min_cost = 0                                                    # This will be our return value
    covered = []                                                    # Control variable for covering all departments
    while covered != departments:                                   # While we didn't cover all the departments
        not_covered_set = set(departments) - set(covered)           # look for not visited department
        not_covered_list = list(not_covered_set)                    # set to list
        path_start = not_covered_list[0]                            # take one department as a start department
        path = dfs(map_of_gtu, path_start)                          # take all departments can be reached from start
        covered.extend(path)                                        # this path will be added to covered
        path_cost = road_cost*(len(path)-1) + lab_cost              # calculate total path_cost for this path
        min_cost += path_cost                                       # add this path's cost to min_cost

    return min_cost                                                 # return min_cost


def labify_tester():
    mapOfGTU1 = {
        1: set([2, 3]),
        2: set([1, 3]),
        3: set([1, 2])
    }  # graph is initialized as dictionary
    min_cost1 = findMinimumCostToLabifyGTU(2, 1, mapOfGTU1)
    print("Min cost of repairing GTU ", min_cost1)
    print ("------------")
    mapOfGTU2 = {
        1: set([2, 3]),
        2: set([1, 3, 4]),
        3: set([1, 2, 4]),
        4: set([3, 2]),
        5: set([6]),
        6: set([5])
    }  # graph is initialized as dictionary
    min_cost2 = findMinimumCostToLabifyGTU(5, 2, mapOfGTU2)
    print("Min cost of repairing GTU ", min_cost2)  # Output will be 18


labify_tester()
