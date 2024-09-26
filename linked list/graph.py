#graph class 3

# undirected and unweighted graph
# class Graph:
#     def __init__(self, noOfNodes):
#         self.noOfNodes = noOfNodes
#         self.AdjMatrix = []
#         for i in range(noOfNodes):
#             row = [0]*noOfNodes
#             self.AdjMatrix.append(row)

#     def addEdge(self, val1, val2):
#         self.AdjMatrix[val1][val2] = 1
#         self.AdjMatrix[val2][val1] = 1

#     def display(self):
#         rows = self.AdjMatrix
#         for row in rows:
#             print(row)

# g = Graph(4)
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(0,3)
# g.addEdge(1,3)
# g.addEdge(1,2)
# g.addEdge(2,3)

# g.display()




#graph class 4

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         newNode = Node(data)
#         if not self.head:
#             self.head = newNode
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newNode

# class Graph:
#     def __init__(self):
#         self.adjList = {}

#     def addEdge(self, val1, val2):
#         if val1 not in self.adjList:
#             self.adjList[val1] = LinkedList()
#         else:
#             self.adjList[val1].append(val2)


#         if val2 not in self.adjList:
#             self.adjList[val2] = LinkedList()
#         else:
#             self.adjList[val2].append(val1)


# g = Graph()
# g.addEdge("hyderabad","vizag")
# g.addEdge("hyderabad","raj")
# g.addEdge("hyderabad","kurnool")
# g.addEdge("hyderabad","guntoor")
# g.addEdge("raj","vijaywada")
# g.addEdge("raj","medak")
# g.addEdge("nellore","raj")


# # print("dcsdvsv")


# for key, value in g.adjList.items():
#     print(key, end = "->")
#     current = value.head
#     while current:
#         print(current.data)
#         current = current.next
#     print("None",end = "->")



#graph class 4
#2

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         newNode = Node(data)
#         if not self.head:
#             self.head = newNode
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newNode

# class Graph:
#     def __init__(self):
#         self.adjList = {}

#     def addEdge(self, val1, val2):
#         if val1 not in self.adjList:
#             self.adjList[val1] = LinkedList()
#         else:
#             self.adjList[val1].append(val2)


#         if val2 not in self.adjList:
#             self.adjList[val2] = LinkedList()
#         else:
#             self.adjList[val2].append(val1)





# g = Graph()
# g.addEdge("0","1")
# g.addEdge("0","5")
# g.addEdge("0","4")
# g.addEdge("0","3")
# g.addEdge("0","2")
# g.addEdge("1","0")
# g.addEdge("1","2")
# g.addEdge("2","0")
# g.addEdge("2","1")
# g.addEdge("2","3")
# g.addEdge("3","0")
# g.addEdge("3","2")
# g.addEdge("3","4")
# g.addEdge("4","0")
# g.addEdge("4","3")
# g.addEdge("4","5")
# g.addEdge("5","0")
# g.addEdge("5","4")


# for key, value in g.adjList.items():
#     print(key, end = "->")
#     current = value.head
#     while current:
#         print(current.data)
#         current = current.next
#     print("None",end = "->")



# Above problem correct explanation
#3


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

# class Graph:
#     def __init__(self):
#         self.adjList = {}

#     def addEdge(self, key1, key2):
#         if key1 not in self.adjList:
#             self.adjList[key1] = LinkedList()
#         self.adjList[key1].append(key2)

#         if key2 not in self.adjList:
#             self.adjList[key2] = LinkedList()
#         self.adjList[key2].append(key1)

# g = Graph()
# g.addEdge("1", "2")
# g.addEdge("1", "3")
# g.addEdge("1", "5")
# g.addEdge("4", "3")
# g.addEdge("4", "2")
# g.addEdge("4", "5")

# # Printing the adjacency list
# for key, value in g.adjList.items():
#     print(key, end=" -> ")
#     current = value.head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")




# issue with the input,

# this is correct< debug it once, we'll continue with it tomorrow


#graph class 7
#1
# def graphDfsPreorder(graph, node, visitedPlaces):
    
#     if node not in visitedPlaces:
#         print(node, end=",")
#         visitedPlaces.add(node)

#         for i in graph[node]:
#             graphDfsPreorder(graph, i, visitedPlaces)

# def graphDfsPostorder(graph, node, visitedPlaces):
    
#     if node not in visitedPlaces:
#         print(node, end=",")
#         visitedPlaces.add(node)

#         for i in graph[node]:
#             graphDfsPreorder(graph, i, visitedPlaces)

# graph = {
#     "A":["C","B"],
#     "B":["A","D","E"],
#     "C":["A"],
#     "D":["B"],
#     "E":["B","F"],
#     "F":["E"]
# }
# node = "F"
# visitedPlaces = set()
# graphDfsPreorder(graph, node, visitedPlaces)

#2
# def graphDfsPreorder(graph, node, visitedPlaces):
    
#     if node not in visitedPlaces:
#         print(node, end=",")
#         visitedPlaces.add(node)

#         for i in graph[node]:
#             graphDfsPreorder(graph, i, visitedPlaces)

# def graphDfsPostorder(graph, node, visitedPlaces):
    
#     if node not in visitedPlaces:
#         # print(node, end=",")
#         visitedPlaces.add(node)

#         for i in graph[node]:
#             graphDfsPreorder(graph, i, visitedPlaces)
#         print(node, end=",")

# graph = {
#     "A":["C","B"],
#     "B":["A","D","E"],
#     "C":["A"],
#     "D":["B"],
#     "E":["B","F"],
#     "F":["E"]
# }
# node = "F"
# visitedPlaces = set()
# # graphDfsPreorder(graph, node, visitedPlaces)
# graphDfsPostorder(graph, node, visitedPlaces)