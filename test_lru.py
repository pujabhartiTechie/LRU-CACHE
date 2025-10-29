from lru_cache import LRUCache

if name == "main":
    print(" Testing LRU Cache")

    cache = LRUCache(2)

    cache.put(1, 10)
    cache.put(2, 20)
    print("Get(1):", cache.get(1)) 

    cache.put(3, 30) 
    print("Get(2):", cache.get(2))  

    cache.put(4, 40) 
    print("Get(1):", cache.get(1))  
    print("Get(3):", cache.get(3))  
    print("Get(4):", cache.get(4)) 
