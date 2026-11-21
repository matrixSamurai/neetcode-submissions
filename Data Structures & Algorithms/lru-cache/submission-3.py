class Node:

    def __init__(self, key = None, value = None, prev = None, nxt = None):

        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):

        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    
    def insertAtHead(self, node):

        self.head.nxt.prev = node
        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt = node


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.removeNode(node)
        self.insertAtHead(node)

        return node.value

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:

            node = self.cache[key]
            node.value = value

            self.removeNode(node)
            self.insertAtHead(node)

            return

        

        newNode = Node(key, value)

        self.cache[key] = newNode
        self.insertAtHead(newNode)

        if self.capacity < len(self.cache):

            tailNode = self.tail.prev

            self.removeNode(tailNode)
            del self.cache[tailNode.key]



        
