# 🗂️ LRU Cache (Least Recently Used)

## 📌 Overview
This project implements an **LRU (Least Recently Used) Cache** using **Python**.  
LRU is a caching technique where the **least recently used item** is removed when the cache is full.

## code structure
lru-cache/
│── lru_cache.py     # LRU Cache implementation
│── test_lru.py      # Example usage & tests
│── README.md        # Documentation

lru_cache.py → Core LRU Cache implementation.
test_lru.py → Some test cases / example runs.
README.md → Explains the project (what is LRU, how to run, sample output).

It combines:
- **HashMap (dictionary)** → O(1) lookups
- **Doubly Linked List** → O(1) insert/remove operations

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lru-cache.git
   cd lru-cache

2. Run the test file:
   python test_lru.py

3. Sample Output
	Testing LRU Cache
	Get(1): 10
	Get(2): -1
	Get(1): -1
	Get(3): 30
	Get(4): 40
