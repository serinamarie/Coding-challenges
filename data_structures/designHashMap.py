# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
  
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash_map[key] = value
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # return v if exists else -1
        return self.hash_map[key] if key in self.hash_map else -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # if exists, remove key with .pop()
        self.hash_map.pop(key, None)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)