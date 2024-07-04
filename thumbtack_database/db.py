class Database:
    def __init__(self):
        self.records = []
        self.count = {}

        self.term = -1

        self.store = {}
        self.count_store = {}

    def get(self, key):
        return self.store.get(key)

    def insert(self, key, value):
        self.store[key] = value

    def unset(self, key):
        del self.store[key]

    def numequalto(self, value):
        return len([k for k, v in self.store.items() if v == value]) or None

    def begin(self):
        self.records.append(self.store.copy())
        self.term += 1

    def commit(self):
        self.records = []
        self.term = -1

    def rollback(self):
        if self.term == -1:
            return "NO TRANSACTION"
        self.store = self.records[self.term]
        self.term -= 1

    def process(self, cmd_info):
        if not getattr(self, cmd_info["command"]):
            raise ValueError("Command not implemented.")

        operation = getattr(self, cmd_info["command"])

        if cmd_info["value"]:
            res = operation(cmd_info["key"], cmd_info["value"])
        elif not cmd_info["key"] and not cmd_info["value"]:
            res = operation()
        else:
            res = operation(cmd_info["key"])

        if cmd_info["get_result"] and res:
            return res
        elif cmd_info["get_result"] and res is None:
            return "Not found."
        else:
            return None
