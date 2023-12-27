class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash = [None for _ in range(size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def add(self, key, val):
        h = self.get_hash(key)
        self.hash[h] = val
    
    def get_item(self, key):
        h = self.get_hash(key)
        return self.hash[h]

    def del_item(self, key):
        h = self.get_hash(key)
        self.hash[h] = None
    
    def print_hash(self):
        print(self.hash)


hsh = HashTable(10)
hsh.add('one', 1)
hsh.add('two', 2)
hsh.add('four', 4)

hsh.print_hash()
print(hsh.del_item('four'))
hsh.print_hash()
