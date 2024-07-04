class Node:
    def __init__(self, num):
        self.next = {}
        self.num = num

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        node_dict = {}
        res = [None for _ in range(len(queries))]


        def __helper(curr_numerator, curr_denominator, curr_seen_elements, curr_product, query_index):
            curr_denominators = node_dict[curr_numerator]

            for denominator in curr_denominators:
                if denominator not in curr_seen_elements:
                    # print(query_index)
                    # print(curr_seen_elements)
                    # print(denominator)
                    # print(curr_product * curr_denominators[denominator])
                    if curr_denominator == denominator:
                        res[query_index] = (curr_product * curr_denominators[denominator])
                    else:
                        curr_seen_elements.add(denominator)
                        __helper(denominator, curr_denominator, curr_seen_elements, curr_product * curr_denominators[denominator], query_index)

            return None


        for i in range(len(equations)):
            numerator, denominator = equations[i]
            curr_ans = values[i]


            if numerator not in node_dict:
                node_dict[numerator] = {}

            node_dict[numerator][denominator] = curr_ans

            if denominator not in node_dict:
                node_dict[denominator] = {}

            node_dict[denominator][numerator] = (1/curr_ans)

        # print(node_dict)

        for query_index, query in enumerate(queries):
            curr_num, curr_dom = query

            if curr_num not in node_dict or curr_dom not in node_dict:
                print()
                if curr_num == curr_dom:
                    res[query_index] = 1.0
                else:
                    res[query_index] = -1.0
                continue

            if curr_num == curr_dom:
                res[query_index] = 1.0
                continue

            __helper(curr_num, curr_dom, set([curr_num]), 1, query_index)

        for i, j in enumerate(res):
            if j == None:
                res[i] = -1

        return(res)


if __name__ == '__main__':
    s = Solution()
    # s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    # s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
    # s.calcEquation([["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]])
    x = s.calcEquation(
        [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
        [3.0,0.5,3.4,5.6],
        [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
    )
    print(x)