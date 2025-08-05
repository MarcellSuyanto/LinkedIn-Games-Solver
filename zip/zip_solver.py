import time

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
        self.paths = [[] for i in range(len(self.map.checkpoints) + 1)]
        self.directions = [(-1,0), (1,0), (0,-1), (0,1)]
        self.route = []

    def find_paths_v1(self):
        for i in range(1, len(self.map.checkpoints)):
            self.path_dfs_v1(self.map.checkpoints[i-1][0], self.map.checkpoints[i-1][1], self.map.checkpoints[i][0], self.map.checkpoints[i][1], [], i)
            print(f'Section {i} done')
        # print(self.paths)
        print("Number of paths: {}".format(sum(len(x) for x in self.paths)))



    def evaluate_v1(self):
        route = []
        print(self.eval_dfs(1, route))

    def eval_dfs(self, section, route):
        if section == len(self.map.checkpoints):
            self.route = list(route)
        else:
            for path in self.paths[section]:
                overlap = False
                for cell in path:
                    if cell in route or cell in self.map.checkpoints[0:section] + self.map.checkpoints[section+1:]:
                        overlap = True
                        break
                if not overlap:
                    for cell in path:
                        route.append(cell)
                    self.eval_dfs(section + 1, route)
                    for cell in path:
                        route.pop(-1)


    def path_dfs_v1(self, cx, cy, ex, ey, path, index):
        if (cx == ex) and (cy == ey):
            self.paths[index].append(list(path))
        else:
            for dx, dy in self.directions:
                if (0 <= cx+dx) and (cx+dx < self.map.size) and (0 <= cy+dy) and (cy+dy < self.map.size) and ((cx+dx,cy+dy) not in path) and len(path) < self.map.size**2 * 0.8:
                    path.append((cx+dx, cy+dy))
                    self.path_dfs_v1(cx+dx, cy+dy, ex, ey, path, index)
                    path.pop(-1)

    def zip_solve_v2(self, sx: int, sy: int, ex: int, ey: int, path, checkpoints):

        # If current coordinates equal target and if current path length = number of tiles
        if (sx == ex) and (sy == ey) and len(path) == self.map.size**2:
            i = 0

            #Check for correct order of checkpoints
            for point in path:
                if list(point) in checkpoints and list(point) == checkpoints[i]:
                    i += 1
            if i == len(checkpoints):
                self.route = list(path)
        else:
            # For 4 cardinal directions, explores in each
            for dx, dy in self.directions:
                if (0 <= sx+dx) and (sx+dx < self.map.size) and (0 <= sy+dy) and (sy+dy < self.map.size) and ((sx+dx,sy+dy) not in path):
                    path.append((sx+dx, sy+dy))
                    self.zip_solve_v2(sx+dx, sy+dy, ex, ey, path, checkpoints)
                    path.pop(-1)


    def show_path(self, path):
        print("+" + "---+" * len(self.map.map))
        for i in range(len(self.map.map)):
            print("|", end="")
            for j in range(len(self.map.map[i])):
                print(" {} |".format("X" if (i, j) in path else " "), end="")
            print("\n+" + "---+" * len(self.map.map[i]))


test = Zip()

#Version 1
# print("Finding Paths...")
# test.find_paths_v1()
# for i in range(1, len(test.paths) - 1):
#     print(f'Section {i}: {len(test.paths[i])} paths')
# print("Evaluating...")
# start = time.time()
# test.evaluate_v1()
# elap = time.time() - start
# print(test.route)
# print(f'Evaluation time: {elap}')

#Version 2
print(f'Evaluating...')
path = [(test.map.checkpoints[0][0], test.map.checkpoints[0][1])]
start = time.time()
test.zip_solve_v2(test.map.checkpoints[0][0], test.map.checkpoints[0][1], test.map.checkpoints[-1][0], test.map.checkpoints[-1][1], path, test.map.checkpoints)
elap = time.time() - start
print(test.route)
print(f'Evaluation time: {elap}')

