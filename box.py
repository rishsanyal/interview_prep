

# * Find number of bits set in a signed number

def count_n_bits(n):
    count = 0

    print("-------")
    while n:
        count += n & 1
        n >>= 1

    print("-------")

    return count

# print(count_n_bits(7)) # 3
# print(count_n_bits(8)) # 1
# print(count_n_bits(9)) # 2

# * There are many files and folders in the file system. Find the largest k integers from all files (assuming that each line in the file is an int) [Kadane’s Algorithm]?

## Read all of the files
## Iterate over all of the files
## Iterate over all of the lines in the file
## Add all of the integers to a list

## quick select with the kth largest number
## Return the kth largest number

def get_kth_largest_number(inp_list, k):
    k = len(inp_list) - k

    def partition(l, r):
        pivot, p = inp_list[r], r

        for i in range(l, r):
            if inp_list[i] >= pivot:
                inp_list[i], inp_list[p] = inp_list[p], inp_list[i]
                p += 1

            if k < p:
                return partition(l, p - 1)
            elif k > p:
                return partition(p + 1, r)
            else:
                return inp_list[p]

    return partition(0, len(inp_list) - 1)

# print(get_kth_largest_number([1, 2, 3, 4, 5], 2)) # 4
# print(get_kth_largest_number([1, 2, 3, 4, 5], 3)) # 3
# print(get_kth_largest_number([1, 2, 3, 4, 5], 1)) # 5