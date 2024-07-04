class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        ## DFS or BFS

        ## Create a graph from i to n


        ## Just make an adjacency list class -> pre-requisites

        ## find all cyclic classes
        ## Num Courses cyclic classes
        if not prerequisites:
            return True

        course_requisites = [[] for _ in range(0, numCourses)]
        cycle_detection = [None for _ in range(0, numCourses)]
        valid_classes = set()

        for i in range(0, numCourses):
            valid_classes.add(i)

        for i, j in prerequisites:
            if course_requisites[i] is not None:
                course_requisites[i].append(j)
            else:
                course_requisites[i] = [j]


        for i in valid_classes:
            curr_class = i

            visited_set = set()

            curr_prerequisites = course_requisites[curr_class]

            if not curr_prerequisites:
                cycle_detection[curr_class] = False

            else:
                while curr_prerequisites:
                    curr_prerequisite = curr_prerequisites.pop()

                    if cycle_detection[curr_prerequisite] == None:
                        if curr_prerequisite in visited_set:
                            cycle_detection[curr_class] = True
                        else:
                            visited_set.add(curr_prerequisite)
                            curr_prerequisites.extend(course_requisites[curr_prerequisite])

                    elif cycle_detection[curr_prerequisite] == True:
                        cycle_detection[curr_class] = True
                    elif cycle_detection[curr_prerequisite] == False:
                        cycle_detection[curr_class] = False
                    else:
                        continue

        return not any(cycle_detection)


test = (2, [[1,0], [0,1]])
# test = (5, [[3,2], [3,4], [0,3], [1, 0], [3, 1]])
# test = (3, [[0,1],[0,2],[1,2]])
s = Solution()
print(s.canFinish(test[0], test[1]))