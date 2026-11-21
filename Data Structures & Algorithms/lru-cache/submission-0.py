class Node:

    def __init__(self,key = None, val = None, prevNode = None, nextNode = None):

        self.key = key
        self.val = val
        self.prevNode = prevNode
        self.nextNode = nextNode


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.nextNode = self.tail
        self.tail.prevNode = self.head
    
    def deleteNode(self, node):

        node.prevNode.nextNode = node.nextNode
        node.nextNode.prevNode = node.prevNode
    
    def insertAtHead(self, node):

        node.nextNode = self.head.nextNode
        node.prevNode = self.head
        self.head.nextNode = node
        node.nextNode.prevNode = node


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.deleteNode(node)

        self.insertAtHead(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        if key in self.cache:

            node = self.cache[key]

            self.deleteNode(node)
            self.insertAtHead(node)

            node.val = value

            return 
        

        newNode = Node(key, value)
        self.cache[key] = newNode

        self.insertAtHead(newNode)

        if self.capacity < len(self.cache):

            del self.cache[self.tail.prevNode.key]
            self.deleteNode(self.tail.prevNode)




        
