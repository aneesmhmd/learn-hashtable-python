class HashTable:

    # Initialize the hash table
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def get_item(self, key):
        idx = self.get_hash(key)
        while self.keys[idx]:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
        return None

    def set_item(self, key, value):
        idx = self.get_hash(key)
        while self.keys[idx]:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.size

        self.keys[idx] = key
        self.values[idx] = value

    def print_hash(self):
        print(self.values)


hashtable = HashTable(10)
hashtable.set_item('one', 1)
hashtable.set_item('two', 2)
hashtable.set_item('three', 3)
hashtable.set_item('four', 4)
print(hashtable.get_item('two'))
hashtable.print_hash()
