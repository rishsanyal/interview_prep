

class Database():
    def __init__(self):
        self.store = {} # Holds all key-value information
        self.count_store = {} # Holds the value - value counter information

        self.terms = []

    # O(1)
    def add(self, key, val):
        if key in self.store:
            prev_val = self.store[key]
            self.count_store[prev_val] = self.count_store.get(prev_val) - 1

            if self.count_store[prev_val] <= 0:
                self.count_store.pop(prev_val)

        self.store[key] = val
        self.count_store[val] = self.count_store.get(val, 0) + 1

    # O(1)
    def get(self, key):
        return self.store.get(key, None)

    # O(1)
    def delete(self, key):
        if key in self.store:
            val = self.store[key]
            self.count_store[val] = self.count_store.get(val) - 1

            if self.count_store[val] <= 0:
                self.count_store.pop(val)

            self.store.pop(key)

    # O(1)
    def count(self, key):
        return self.count_store.get(key, 0)

    # O(1)
    def begin(self):
        # We're storing snapshots for now
        self.terms.append(
            (
                self.store.copy(),
                self.count_store.copy()
            )
        )

    # O(1)
    def commit(self):
        self.terms = []

    # O(1)
    def rollback(self):
        if not self.terms:
            print("NO TRANSACTION")
        else:
            prev_store, prev_count_store = self.terms[-1]

            self.store = prev_store
            self.count_store = prev_count_store

            self.terms.pop()

if __name__ == "__main__":
    database = Database()

    # database.add("a", 10)
    # print(database.get("a"))

    # database.delete("a")
    # print(database.get("a"))

    # database.add("a", 10)
    # database.add("b", 10)
    # print(database.count(10)) # 2

    # print(database.count(20)) # 0

    # database.delete("a")
    # print(database.count(10)) # 1

    # database.add("b", 30)
    # print(database.count(10)) # 0


    # database.begin()

    # database.add("a", 30)
    # print(database.get("a")) #  30

    # database.begin()

    # database.add("a", 40)
    # print(database.get("a")) # 40

    # database.commit()
    # print(database.get("a")) # 40

    # database.rollback()
    # # print(database.get("a")) # None

    # database.add("a", 50)
    # database.begin()
    # print(database.get("a")) #  50

    # database.add("a", 60)
    # database.begin()
    # database.delete("a")
    # print(database.get("a")) # None

    # database.rollback()
    # print(database.get("a")) # 60

    # database.commit()
    # print(database.get("a")) # 60


    database.add("a", 10)
    database.begin()
    print(database.count(10)) #  1

    database.begin()
    database.delete("a")
    print(database.count(10)) #  0

    database.rollback()
    print(database.count(10)) #  1




"""
{
    a: 10
    b: 20
}

{
    10: 1,
    20: 1
}

BEGIN -> self.terms.append( (self.store.copy(), self.count.copy()) ), self.terms += 1

{
    a: 10
}
{
    10: 1
}

SET a 10
BEGIN
DELETE a
ROLLBACK
GET a


{
    a: 10
}
{
    10: 1
}

BEGIN -> [({a: 10}{10: 1})], increase the term number
self.store is the same

delete -> self.store is empty

Rollback -> self.store = self.terms[-1]
Get a -> get from self.store -> a: 10
"""

"""

SET a 10
BEGIN
DELETE a
COMMIT
GET a


{
    a: 10
}
{
    10: 1
}

BEGIN -> [({a: 10}{10: 1})], increase the term number
self.store is the same

delete -> self.store is empty

COMMIT -> current self.store becomes permanent (delete everything in self.terms, if self.terms is empty, we cannot rollback -> No transaction)
Get a -> NULL
"""



"""
Think about storing without copying the dictionaries twice

(incrementally storing information)

SET a 10
BEGIN
SET b 20
DELETE a
ROLLBACK
GET a


{
    a: 10
}
{
    10: 1
}

BEGIN -> [({a: 10}{10: 1})], increase the term number
self.store is the same

SET b 20:
we add the information to self.store and self.value_ctr


self.store =>
{
    a: 10
    b: 20
}

{
    10: 1,
    20: 1
}

delete a -> self.store is empty

self.store =>
{
    b: 20
}
{
    20: 1
}

Rollback -> We go through all the snapshots to create the new self.store

We have an empty self.store and self.value_counter
for every transactional block (self.terms)
    we update the dictionary

self.store and self.value_counter

self.store =>
{
    a: 10
}

{
    10: 1,
}

Get a -> get from self.store -> a: 10
"""

"""
{
    b: 20
}
{
    20: 1
}

all transactions -> []
curr -> [set b 20]


BEGIN
{
    b: 20
    c: 10
}
{
    20: 1
    10: 1
}

all transactions -> [set b 20]
curr_transaction -> [set c 20]

ROLLBACK
We go through all_transactions in order -> Create self.store from that

all transactions -> [set b 20, begin, set b 30, set b 40, delete b] [Enhancement]
"""