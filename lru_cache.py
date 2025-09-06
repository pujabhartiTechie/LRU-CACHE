class Node:
    """Doubly linked list node used in LRU Cache."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation.
    Uses a combination of HashMap + Doubly Linked List.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key -> Node

        # Dummy head and tail (to avoid edge cases)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove node from linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node: Node):
        """Add node to the end (most recently used)."""
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        """Return value if key exists, else -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)  # Move to most recent
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Insert or update value, evict least recently used if full."""
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove LRU from head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
