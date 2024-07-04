def bs(search_num, power, strengths):
    if not strengths:
        return 0

    l, r = 0, len(strengths) - 1
    idx = 0

    while l <= r:
        mid_num = (l + r) // 2
        if strengths[mid_num] * power < search_num:
            l = mid_num + 1
        else:
            r = mid_num - 1
            idx = mid_num

    return len(strengths) - idx

        # if (l,r) in visited:
        #     break



print(bs(7, 1, [5,10,15,20,25]))
# print(bs(7, [5,7, 10,15,20,25]))
# print(bs(7, [1,2,3,4,5,6]))
# print(bs(7, [1,1,1,5,7,10]))


# print(bs(7, [1,2,3,4,5,6]))