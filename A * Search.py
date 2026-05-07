import heapq

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

class Node:
    def __init__(self, state, g=0, parent=None, move=""):
        self.state = state
        self.g = g
        self.parent = parent
        self.move = move
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        # Manhattan Distance
        d = 0
        for i in range(3):
            for j in range(3):
                val = self.state[i][j]
                if val != 0:
                    x, y = (val-1)//3, (val-1)%3
                    d += abs(i-x) + abs(j-y)
        return d

    def is_goal(self):
        return self.state == GOAL

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_neighbors(self):
        x, y = self.find_blank()
        moves = {
            "Up": (x-1, y),
            "Down": (x+1, y),
            "Left": (x, y-1),
            "Right": (x, y+1)
        }

        neighbors = []
        for m, (nx, ny) in moves.items():
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [row[:] for row in self.state]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                neighbors.append(Node(new, self.g+1, self, m))
        return neighbors

    def __lt__(self, other):
        return self.f < other.f


def astar(start):
    open_list = []
    visited = set()

    heapq.heappush(open_list, Node(start))

    while open_list:
        node = heapq.heappop(open_list)

        if node.is_goal():
            return node

        visited.add(str(node.state))

        for child in node.get_neighbors():
            if str(child.state) not in visited:
                heapq.heappush(open_list, child)

    return None


def print_solution(goal):
    path = []
    while goal:
        path.append(goal)
        goal = goal.parent

    path.reverse()

    print("Moves to solve:")
    for step in path:
        print(step.move)
        for row in step.state:
            print(row)
        print()


# Given Initial State
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

result = astar(start)

if result:
    print_solution(result)
else:
    print("No solution found")
