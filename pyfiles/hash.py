class Entry:
    """
    Used by the ListMapping class to store keys and their values

    Created by Justin Elak
    """
    def __init__(self, key, item):
        self.key = key
        self.item = item

    def __str__(self):
        return f"{self.key} : {self.item}"

class ListMapping:
    """
    Used by HashMap in order to avoid hash collision by using separate chaining

    Created by Justin Elak
    """
    def __init__(self):
        self._entries = []

    def put(self, key, item):
        for entry in self._entries:
            if entry.key == key:
                entry.item = item
                return
        self._entries.append(Entry(key, item))

    def get(self, key):
        for entry in self._entries:
            if entry.key == key:
                return entry.item
        raise KeyError

    def __contains__(self, key):
        for entry in self._entries:
            if entry.key == key:
                return True
        return False

    def items(self):
        return ((e.key, e.item) for e in self._entries)

class HashMap:
    """
    Standard hashmap similar to Python stand one, uses separate changing to handle hash collisions

    Created by Justin Elak
    """
    def __init__(self, size=2):
        self._size = size
        self._buckets = [ListMapping() for _ in range(self._size)]
        self._length = 0

    def __setitem__(self, key, value):
        bucket = self._buckets[hash(key) % self._size]
        if key not in bucket:
            self._length += 1
        bucket.put(key, value)

        if self._length / self._size > 0.75:
            self._rehash()

    def put(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        bucket = self._buckets[hash(key) % self._size]
        return bucket.get(key)

    def get(self, key):
        return self[key]

    def __len__(self):
        return self._length

    def __contains__(self, key):
        return key in self._bucket(key)

    def _bucket(self, key):
        return self._buckets[hash(key) % self._size]

    def _rehash(self):
        old = self._buckets
        self._size *= 2
        self._buckets = [ListMapping() for _ in range(self._size)]
        self._length = 0

        for bucket in old:
            for key, item in bucket.items():
                self[key] = item

if __name__ == "__main__":
    thash = HashMap()
    thash["foobar"] = 2
    print(thash["foobar"])