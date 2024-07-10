
# Thoughts:
# We don't want the program's memory to double everytime we usea  begin
# Start by implementing SET,GET, DELETE, COUNT
# Implement Commit, ROllback, Begin later

# Use a dictionary/hash map for storing information -> O(1) lookup
# Count -> Loop through every key, val -> Dictionary mapping Value: Value's count -> O(1) Count
# Design - Highlevel
# Pass in command,store/process commands, Get results
# main.py [ENHANCEMENT]

# interface.py -> Responsible for interacting with the user
# command.py -> Responsible for parsing the command and returning a result for processing ("Set a 10 -> (SET A 10)")
# database.py [Implement this first] -> Responsible for storing information and performing operations on the core datastructure(s)
# (eventually this is where rollback, commit and begin are implemented)

# Database class
# store = {} # Holds all


# List -> To track current term
# We could store the delta between terms
# On rollback we update the current term dict


# all transactions -> [set b 20, begin, set b 30, set b 40, delete b] [Enhancement]

self.store is only updated in commit

How do we optimize for

delete -> delete key
count -> return count

BEGIN -> current ops = [
    set a 10,
    del a
]

we iterate through all of these in reverse
all_ops = [[op1], [op2] ,,...]


self.store  -> {}
# Set a 10

curr_ops = [set a 10, set a 20, delete a]
all_ops = [[]]

Get ->
    go through curr_ops in reverse and for that key,
    if we see a delete first, we return None,
    if we see a set, we return value

Commit -> self.store we create from all_ops(in reverse) and then curr_ops (in reverse) (slightly expensive)
[TIP: Use a dictionary to store all ops]

Rollback -> we pop(-1) from all_ops and make that curr_ops

Begin -> all_ops.append(curr_ops), curr_ops = []