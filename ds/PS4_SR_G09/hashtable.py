import re

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self._keys = []

    def put(self, key, data):
        hashvalue = self.HashId(key)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace
        self._keys.append(key)

    def get(self, key):
        startslot = self.HashId(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def HashId(self, key):
        size = len(self.slots)
        digits = re.findall(r'\d+', key)
        digit = "".join(digits)
        return int(digit) % size

    def rehash(self, oldhash):
        size = len(self.slots)
        return int(oldhash + 1) % size

    def keys(self):
        return set(self._keys)

    def clear(self):
        self.slots = None
        self.data = None
        self._keys = None