class Solution:
    """
    From Lintcode
    """
    def shortestPath(self, grid, source, destination):

        if not grid or not grid[0]:
            return -1

        steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), 
        (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]

        queue = collections.deque([source])
        visited = set([source])

        distince = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == destination:
                    return distance

                for delta_x, delta_y in steps:
                    next_x, next_y = x + delta_x, y + delta_y
                    if not self.is_valid(grid, next_x, next_y, visited):
                        continue
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

        return -1

    def is_valid(self, grid, x, y, visited):

        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == 0
