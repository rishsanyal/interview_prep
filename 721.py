from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        ## { id: name}
        ## {id: set (email_ids)}

        ## insert(name, emails)
        ##  - get all ids by name
        ##  - If overlap with any email ids for those ids, add all emails to email_ids
        ##  - If overlap with multiple ids, merge all those emails to single id,
        ## remove all but that merged id from the first dict

        ## return the list

        name_tracker = {} ## { id: name}
        email_tracker = {} ## {id: set (email_ids)}
        curr_id = 0

        def insert(name, emails):        ## insert(name, emails)
            ##  - get all ids by name
            ##  - If overlap with any email ids for those ids, add all emails to email_ids
            ##  - If overlap with multiple ids, merge all those emails to single id,
            ## remove all but that merged id from the first dict

            nonlocal curr_id

            id_set = set()

            email_set = set(emails)

            for temp_curr_id, curr_name in name_tracker.items():
                if name == curr_name:
                    id_set.add(temp_curr_id)

            similar_ids = set()

            for similar_name_id in id_set:
                if email_set.intersection(set(email_tracker[similar_name_id])):
                    similar_ids.add(similar_name_id)

            if not similar_ids:
                name_tracker[curr_id] = name
                email_tracker[curr_id] = set(emails)
                curr_id += 1
            else:
                golden_id = similar_ids.pop()



                for curr_similar_id in similar_ids:
                    email_tracker[golden_id] = email_tracker[golden_id].union(email_tracker[curr_similar_id])

                    if curr_similar_id != golden_id:
                        name_tracker.pop(curr_similar_id, None)
                        email_tracker.pop(curr_similar_id, None)

                email_tracker[golden_id] = email_tracker[golden_id].union(email_set)

            return None

        def result():
            ## Return pretty result
            result_list = []

            for name_id, name in name_tracker.items():
                temp_list = [name]
                email_list = sorted(list(email_tracker[name_id]))

                temp_list.extend(email_list)

                result_list.append(temp_list)

            return result_list

        for inputAccountInfo in accounts:
            name = inputAccountInfo[0]
            emails = inputAccountInfo[1:]

            insert(name, emails)

        return result()


if __name__ == "__main__":
    s = Solution()
    x = s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])

    print(x)