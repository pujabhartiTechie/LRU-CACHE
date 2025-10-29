from lru_cache import LRUCache

if __name__ == "__main__":
    print(" Testing LRU Cache")

    cache = LRUCache(2)  # capacity = 2

    cache.put(1, 10)
    cache.put(2, 20)
    print("Get(1):", cache.get(1))  # returns 10

    cache.put(3, 30)  # removes key 2
    print("Get(2):", cache.get(2))  # returns -1 (not found)

    cache.put(4, 40)  # removes key 1
    print("Get(1):", cache.get(1))  # returns -1 (not found)
    print("Get(3):", cache.get(3))  # returns 30
    print("Get(4):", cache.get(4))  # returns 40
