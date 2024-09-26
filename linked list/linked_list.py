'''
delete
delete from anywhere
add element anywhere
'''

#linked list class 2

# class Head:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None # also we can say we have initialised empty LL

#     def append(self, data):
#         newHead = Head(data)
#         if self.head == None:
#             self.head = newHead
#             return
#         else:
#             current = self.head # obj avinash avi-->None
#             while current.next is not None:
#                 current = current.next
#             else:
#                 current.next = newHead

#     def prepend(self,data):
#         newHead = Head(data)
#         newHead.next = self.head
#         self.head = newHead

#     def delete(self, data): # nav->ven->manisha->None
        
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         else:
#             current = self.head # obj Naveen
#             while current.next is not None:
#                 if current.next.data == data:
#                     current.next = current.next.next
#                     return
                
#                 current=current.next

#     def displayLL(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end="-->")
#             current = current.next
#         print('None')

# ll = LinkedList()
# ll.append("Avinash")
# ll.append("Venkateshwar")
# ll.append("Manisha")
# ll.prepend("Naveen")
# ll.displayLL()
# ll.delete('Avinash')
# ll.displayLL()


#linked list class 3

#2
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add(self, newData):
#         newNode = Node(newData)
#         if self.head is None:
#             self.head = newNode
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = newNode

#     def bubbleSort(self):
#         if self.head is None:
#             return
#         end = None
#         while end!=self.head:
#             prev = None
#             current = self.head
#             while current.next !=end:
#                 nextNode = current.next
#                 # if nextNode == "None":
#                 #     print("None")
#                 # else:
#                 #     print(nextNode)
#                 if current.data> nextNode.data:
#                     current.next = nextNode.next
#                     nextNode.next = current
#                     if prev:
#                         prev.next = nextNode
#                     else:
#                         self.head = nextNode
#                     current, nextNode = nextNode, current
#                 prev = current
#                 current = nextNode
#             end = current


#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end = "-->")
#             current = current.next
#         print('None')        



# linked_list = LinkedList()
# linked_list.add(5)
# linked_list.add(3)
# linked_list.add(8)
# linked_list.add(1)
# linked_list.add(6)
# linked_list.add(2)

# print("before sorting of linked list: \n")
# linked_list.display()

# linked_list.bubbleSort()

# print("after sorting of linked list: \n")
# linked_list.display()