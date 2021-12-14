

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = None
    
class linkedList:
    def __init__(self,head= None):
        self.head = head
    
    def insert(self,value):
        node = linkedListNode(value)
        if self.head is None:#empty list
            self.head = node #new node becomes the head
            return
        currentNode = self.head #create a pointer starts at head
        while True:
            if currentNode.nextNode is None: #if node is tail
                currentNode.nextNode = node 
                break # at tail therefore break
            currentNode = currentNode.nextNode #transverse the linked List
            
    def printlinkedList(self):
        #need to transverse through array 
        currentNode = self.head #pointer to head
        while currentNode is not None:
            print(currentNode.value, "->", end="")
            currentNode = currentNode.nextNode #transverse
        print(" None")
        # while True:
        #     if currentNode is not None:
        #         print(currentNode.value,"->")
        #         currentNode = currentNode.nextNode #transverse linked list
        #     print("None")
            
 

#initialize linked list
ll = linkedList()
ll.printlinkedList
ll.insert("3")
ll.insert("4")
ll.insert("77")
ll.printlinkedList()       
# 3 -> 7 -> 10

# node1 = linkedListNode(3)
# node2 = linkedListNode(7)
# node3 = linkedListNode(10)
        
# #connect them together 
# node1.nextNode = node2 #node1 3-> node2 7
# node2.nextNode = node3 


# currentNode = node1    
# while True:
#     print(currentNode.value, "->", end = "") 
#     if currentNode.nextNode is None:
#         print("NONE")
#         break
#     currentNode = currentNode.nextNode
    