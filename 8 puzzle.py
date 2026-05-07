import heapq

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

class Puzzle:
    def __init__(self, state, g=0, parent=None):
        self.state = state
        self.g = g
        self.parent = parent
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        dist = 0
        for i in range(3):
            for j in range(3):
                val = self.state[i][j]
                if val != 0:
                    x, y = (val-1)//3, (val-1)%3
                    dist += abs(i-x) + abs(j-y)
        return dist

    def is_goal(self):
        return self.state == GOAL

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def successors(self):
        x, y = self.find_zero()
        moves = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        result = []

        for nx, ny in moves:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [row[:] for row in self.state]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                result.append(Puzzle(new, self.g+1, self))

        return result

    def __lt__(self, other):
        return self.f < other.f


def astar(start_state):
    open_list = []
    heapq.heappush(open_list, Puzzle(start_state))
    visited = set()

    while open_list:
        node = heapq.heappop(open_list)

        if node.is_goal():
            return node

        visited.add(str(node.state))

        for child in node.successors():
            if str(child.state) not in visited:
                heapq.heappush(open_list, child)

    return None


def print_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()

    for step in path:
        for row in step:
            print(row)
        print()
