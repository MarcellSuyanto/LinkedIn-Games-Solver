
class Cell:

    def __init__(self):
        self.walls = 0
        self.index = " "

    def set_checkpoint(self, index):
        self.index = index

class Map:

    def __init__(self):
        self.size = int(input())
        self.map = [[Cell() for i in range(self.size)] for j in range(self.size)]
        self.checkpoints = []
        for i in range(int(input())):
            self.checkpoints.append([int(x) for x in input().split()])
            self.map[self.checkpoints[-1][0]][self.checkpoints[-1][1]].set_checkpoint(i+1)

    def show_map(self):
        print("+" + "---+" * len(self.map))
        for i in range(len(self.map)):
            print("|", end="")
            for j in range(len(self.map[i])):
                print(" {} |".format(self.map[i][j].index), end="")
            print("\n+" + "---+" * len(self.map[i]))

class Zip:

    def __init__(self):
        print("Solving LinkedIn ZIP minigame")
        self.map = Map()
        self.map.show_map()
        self.paths = [[] for i in range(self.map.size)]
        self.directions = [(-1,0), (1,0), (0,-1), (0,1)]

    def find_paths(self):
        for i in range(1, len(self.map.checkpoints)):
            self.dfs(self.map.checkpoints[i-1][0], self.map.checkpoints[i-1][1], self.map.checkpoints[i][0], self.map.checkpoints[i][1], [], i)
        # print(self.paths)
        print("Number of paths: {}".format(len(self.paths[1])))

    def dfs(self, cx, cy, ex, ey, path, index):
        if (cx == ex) and (cy == ey):
            self.paths[index].append(list(path))
        else:
            for dx, dy in self.directions:
                if (0 <= cx+dx) and (cx+dx < self.map.size) and (0 <= cy+dy) and (cy+dy < self.map.size) and ((cx+dx,cy+dy) not in path) and len(path) < self.map.size**2 * 0.8:
                    path.append((cx+dx, cy+dy))
                    self.dfs(cx+dx, cy+dy, ex, ey, path, index)
                    path.pop(-1)

    def show_path(self, path):
        print("+" + "---+" * len(self.map.map))
        for i in range(len(self.map.map)):
            print("|", end="")
            for j in range(len(self.map.map[i])):
                print(" {} |".format("X" if (i, j) in path else " "), end="")
            print("\n+" + "---+" * len(self.map.map[i]))


test = Zip()
test.find_paths()
for path in test.paths[2]:
    print(path)
    test.show_path(path)

print(f'Section 1: {len(test.paths[1])} paths')
print(f'Section 2: {len(test.paths[2])} paths')

