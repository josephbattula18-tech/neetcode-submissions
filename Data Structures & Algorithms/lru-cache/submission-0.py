class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = Node()   # LRU side
        self.tail = Node()   # MRU side

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert node just before tail (MRU position)
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as most recently used
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.val = value

            # Move to MRU
            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.cache[key] = node

            # Insert as MRU
            self.insert(node)

            # Remove LRU if capacity exceeded
            if len(self.cache) > self.capacity:
                lru = self.head.next

                self.remove(lru)
                del self.cache[lru.key]