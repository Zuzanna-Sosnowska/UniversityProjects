class Hashmap:
    def __init__(self, hash_f, n):
        self._len = n
        self._array = n * [None]
        self._hash_f = hash_f
        self._hash_g = None
        self.collision_detecting = self.chaining

    def insert_key(self, key):
        index = self._hash_f(key)
        self.collision_detecting(index, key)

    def chaining(self, index, key):
        if self._array[index] is None:
            self._array[index] = [key]
        elif key not in self._array[index]:
            self._array[index].append(key)

    def linear_probing(self, index, key):
        i = index
        while self._array[i] is not None:
            i = (i+1) % self._len
            if i == index:
                raise Exception('Tablica asocjacyjna jest pełna!')
        self._array[i] = key

    def other_hash_function(self, index, key):
        if self._arr[self._f(key)] is not None:
            for i in range(1, self._n + 1):
                j = (self._f(key) + i * self._g(key)) % self._n
                if self._arr[j] is None:
                    self._arr[j] = key
                    break
        else:
            self._arr[self._f(key)] = key

    def set_collision_detecting_to_chaining(self):
        self.collision_detecting = self.chaining

    def set_collision_detecting_to_linear_probing(self):
        self.collision_detecting = self.linear_probing

    def set_collision_detecting_to_other_hash_function(self, hash_g):
        self.collision_detecting = self.other_hash_function
        self._hash_g = hash_g

    def __str__(self):
        return str(self._array)

    def clear(self):
        for i in range(self._len):
            self._array[i] = None


if __name__ == '__main__':
    hash_map = Hashmap(lambda x: (3*x+5) % 11, 11)
    keys_1 = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
    for key in keys_1:
        hash_map.insert_key(key)
    print(hash_map)

    hash_map.set_collision_detecting_to_linear_probing()
    hash_map.clear()
    for key in keys_1:
        hash_map.insert_key(key)
    print(hash_map)

    hash_map.set_collision_detecting_to_other_hash_function(lambda x: 7 - (x % 7))
    hash_map.clear()
    for key in keys_1:
        hash_map.insert_key(key)
    print(hash_map)
