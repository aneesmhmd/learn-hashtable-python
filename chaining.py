class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash = [[] for _ in range(size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h %  self.size
    
    def set_item(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.hash[h]):
            if element[0] == key:
                self.hash[h][idx] = (key, value)
                found = True
        if not found:
            self.hash[h].append((key, value))

    def get_item(self, key):
        h = self.get_hash(key)
        for element in self.hash[h]:
            if element[0] == key:
                return element[1]
        return None

    def print(self):
        print(self.hash)

table = HashTable(10)
table.set_item('one', 1)
table.set_item('two', 2)
table.set_item('three', 3)
table.set_item('four', 4)
print(table.get_item('two'))
table.print()