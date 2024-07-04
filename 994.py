class Solution(object):

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        fresh_orange_set = set()
        rotten_orange_set = set()
        total_oranges = 0

        for x_index, x_value in enumerate(grid):
            for y_index, y_value in enumerate(x_value):
                if y_value == 1:
                    fresh_orange_set.add((x_index, y_index))

                if y_value == 2:
                    rotten_orange_set.add((x_index, y_index))

                if y_value != 0:
                    total_oranges += 1

        def check_if_orange_can_be_rotten(x, y):
            if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):
                if grid[x][y] != 1:
                    return False
                else:
                    grid[x][y] = 2
                    return True
            else:
                return False

        curr_time = 0
        newly_rotten_oranges = set()
        newly_rotten_oranges_count = len(rotten_orange_set)

        while rotten_orange_set:
            curr_rotten_orange_x, curr_rotten_orange_y  = rotten_orange_set.pop()

            if check_if_orange_can_be_rotten(curr_rotten_orange_x-1, curr_rotten_orange_y):
                newly_rotten_oranges.add((curr_rotten_orange_x-1, curr_rotten_orange_y))

            if check_if_orange_can_be_rotten(curr_rotten_orange_x, curr_rotten_orange_y-1):
                newly_rotten_oranges.add((curr_rotten_orange_x, curr_rotten_orange_y-1))

            if check_if_orange_can_be_rotten(curr_rotten_orange_x+1, curr_rotten_orange_y):
                newly_rotten_oranges.add((curr_rotten_orange_x+1, curr_rotten_orange_y))

            if check_if_orange_can_be_rotten(curr_rotten_orange_x, curr_rotten_orange_y+1):
                newly_rotten_oranges.add((curr_rotten_orange_x, curr_rotten_orange_y+1))

            if not rotten_orange_set and newly_rotten_oranges:

                print(newly_rotten_oranges)

                curr_time += 1
                rotten_orange_set = newly_rotten_oranges
                newly_rotten_oranges_count += len(newly_rotten_oranges)

                newly_rotten_oranges = set()

        if newly_rotten_oranges_count == total_oranges or (total_oranges == 0):
            return curr_time

        return -1

# 0 representing an empty cell,
# 1 representing a fresh orange,
# 2 representing a rotten orange.


s = Solution()

# inp_array = [[2,1,1],[1,1,0],[0,1,1]]
inp_array = [[]]

print(s.orangesRotting(inp_array))
