class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        if not maze or entrance[0] >= len(maze) or entrance[1] >= len(maze[0]):
            return 0

        visited_set = set()

        def iterate_through_maze(curr_positions, visited_set):
            min_steps = float('inf')
            curr_steps=0

            intermediate_positions = []

            while curr_positions:
                curr_position = curr_positions.pop(0)

                if (curr_position[0], curr_position[1]) not in visited_set:
                    visited_set.add((curr_position[0], curr_position[1]))

                    if (curr_position[0] >= len(maze) or curr_position[1] >= len(maze[0]) or curr_position[0] < 0 or curr_position[1] < 0):
                        print("oob: ", curr_position)
                    else:
                            if maze[curr_position[0]][curr_position[1]] == "+":
                                print("deadend: {}".format(curr_position))

                            else:
                                if (curr_position[0] == len(maze)-1 or curr_position[1] == len(maze[0])-1 or curr_position[0] == 0 or curr_position[1] == 0) and curr_position != entrance:
                                    print("winner: {}, steps {}, min_steps {}".format(curr_position, curr_steps, min_steps))
                                    min_steps = min(curr_steps, min_steps)

                                    if min_steps == 1:
                                        return min_steps

                                x, y = curr_position
                                intermediate_positions.append([x+1, y])
                                intermediate_positions.append([x, y+1])
                                intermediate_positions.append([x-1, y])
                                intermediate_positions.append([x, y-1])

                if not curr_positions:
                    curr_steps += 1
                    curr_positions.extend(intermediate_positions)
                    intermediate_positions = []

            return min_steps

        steps=float('inf')
        steps = iterate_through_maze([entrance], visited_set)

        # print(visited_set)

        if steps == float('inf'):
            return -1

        return steps







s = Solution()

# inp_list = [[".","+","+","+",".",".",".","+","+"],[".",".","+",".","+",".","+","+","."],[".",".","+",".",".",".",".",".","."],[".","+",".",".","+","+",".","+","."],[".",".",".",".",".",".",".","+","."],[".",".",".",".",".",".",".",".","."],[".",".",".","+",".",".",".",".","."],[".",".",".",".",".",".",".",".","+"],["+",".",".",".","+",".",".",".","."]]

# print(s.nearestExit(inp_list, [5, 6]))

inp_list = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
entrance = [0, 1]

print(s.nearestExit(inp_list, entrance))

# print(len(x))
# print(len(x[0]))

# inp_list[entrance[0]][entrance[1]] = 0

# for i in inp_list:
#     print(i)