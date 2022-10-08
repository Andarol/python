# Task1
# Modify the `depth-first search` to
# produce strongly connected components (Strongly Connected Components ).
# Using a Python dictionary to act as an adjacency list


class Graph:
    def __init__(self):
        self.tops = {}
        self.visited_dfs = set()
        self.visited_bfs = []
        self.queue = []

    def add_tops(self, top):
        self.tops[top] = []

    def add_side(self, top, top_of_side):
        self.tops[top].append(top_of_side)

    def dfs(self, start_top):
        if start_top not in self.visited_dfs:
            print(start_top)
            self.visited_dfs.add(start_top)
            for neighbour in self.tops[start_top]:
                self.dfs(neighbour)

    def the_shortest_search(self, start_point, end_point):
        path_list = [[start_point]]
        path_index = 0
        # To keep track of previously visited nodes
        previous_nodes = {start_point}
        if start_point == end_point:
            return path_list[0]

        while path_index < len(path_list):
            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = self.tops[last_node]

            if end_point in next_nodes:
                current_path.append(end_point)
                return current_path

            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)

                    previous_nodes.add(next_node)

            path_index += 1

        return []

    def bfs(self, start_top):
        self.visited_bfs.append(start_top)
        self.queue.append(start_top)

        while self.queue:
            s = self.queue.pop(0)
            print(s, end=" ")

            for neighbour in self.tops[s]:
                if neighbour not in self.visited_bfs:
                    self.visited_bfs.append(neighbour)
                    self.queue.append(neighbour)


g = Graph()
g.add_tops('1')
g.add_tops('2')
g.add_tops('3')
g.add_tops('4')
g.add_tops('5')
g.add_tops('6')
g.add_tops('7')
g.add_tops('8')
g.add_tops('9')
g.add_tops('10')
g.add_tops('11')
g.add_tops('12')
g.add_side('1', '2')
g.add_side('1', '3')
g.add_side('1', '4')
g.add_side('2', '5')
g.add_side('2', '6')
g.add_side('3', '1')
g.add_side('4', '1')
g.add_side('4', '7')
g.add_side('4', '8')
g.add_side('5', '2')
g.add_side('5', '9')
g.add_side('5', '10')
g.add_side('6', '2')
g.add_side('7', '4')
g.add_side('7', '11')
g.add_side('7', '12')
g.add_side('8', '4')
g.add_side('9', '5')
g.add_side('10', '5')
g.add_side('11', '7')
g.add_side('12', '7')
g.dfs('1')
g.bfs('1')
print('\n', g.the_shortest_search('1', '12'))
# task2
# Using breadth-first search
# write an algorithm that can determine the shortest
# path from each vertex to every other vertex.
# This is called the all-pairs shortest path problem.
