# BFS and DFS, when we are at a node, we can consider any of the adjacent as next node. So both BFS and
# DFS blindly explore paths without considering any cost function. The idea of Best First Search is to use
# an evaluation function to decide which adjacent is most promising and then explore. Best First Searchfalls
# under the category of Heuristic Search or Informed Search. We use a priority queue or heap to store costs
# of nodes which have lowest evaluation function value. So the implementation is a variation of BFS, we
# just need to change Queue to PriorityQueue. We will see more of its working in the solve example.

# The heuristic function used in your Best-First Search (BFS) algorithm is based on the Manhattan
# Distance.
# The Manhattan Distance between two points (x1, y1) and (x2, y2) is given by:
# h(n)=∣x2−x1∣+∣y2−y1∣h(n) = |x2 - x1| + |y2 - y1|
# h(n)=∣x2−x1∣+∣y2−y1∣
# where:
# • (x1,y1)(x_1, y_1)(x1,y1) is the current node,
# • (x2,y2)(x_2, y_2)(x2,y2) is the goal node,
# • h(n)h(n)h(n) is the heuristic cost.


# Apply Best first search for 3 by 3 gird.

# (0,0) | (0,1) | (0,2)

# (1,0) | (1,1) | (1,2)

# (2,0) | (2,1) | (2,2)

import heapq

def best_first_search(grid, start, goal, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()

    while pq:
        h_value, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(f"Visiting: {node} (h={h_value})")
        visited.add(node)

        if node == goal:
            print("Goal reached!")
            return
        
        x,y = node
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for neighbor in neighbors:
            if neighbor in grid and neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

grid = {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}
heuristic = {(0,0):4, (0,1):3, (0,2):2, (1,0):3, (1,1):2, (1,2):1, (2,0):2, (2,1):1, (2,2):0}

best_first_search(grid, (0,0), (2,2), heuristic)