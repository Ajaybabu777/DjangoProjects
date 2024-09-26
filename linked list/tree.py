
# Tree class 1

# class Node:
#     def __init__(self,item):
#         self.item = item
#         self.right = None
#         self.left = None

# def preorder(root):
#     if root is not None:
#         print(root.item)
#         preorder(root.left)
#         preorder(root.right)

# def inorder(root):
#     if root is not None:
#         inorder(root.left)
#         print(root.item)
#         inorder(root.right)



# def postorder(root):
#     if root is not None:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.item)


#     # def postorder(root):

# rootNode = Node(1)
# rootNode.left = Node(2)
# rootNode.right = Node(3)
# rootNode.left.left = Node(5)
# rootNode.left.right = Node(4)
# rootNode.right.right = Node(8)

# # preorder(rootNode)
# postorder(rootNode)


# class 2
# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None
        
# def isBalanced(root):
#     def height(node):
#         if not node:
#             return("empty tree")
#         else:
#             leftHeight = height(node.left)
#             rightHeight = height(node.right)
#             return max(leftHeight,rightHeight)+1
        
#     def checkBalanced(node):
#         if not node:
#             return("empty tree")
#         else:
#             leftHeight = height(node.left)
#             rightHeight = height(node.right)
#             if abs(leftHeight-rightHeight)<=1:
#                 return checkBalanced and checkBalanced(node.right)
#             else:
#                 return("not balaced")
#     return(checkBalanced(root))




# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right = TreeNode(5)


# print(isBalanced(root))

#Trees class 3
# class Node:

# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None


#tree class 3

# def height(node):
# 	if node is None:
# 		return 0
# 	sum = 1 + max(height(node.left), height(node.right))
# 	# print(sum)
# 	return sum


# def diameter(root):

# 	if root is None:
# 		return 0

# 	lheight = height(root.left)
# 	rheight = height(root.right)

# 	ldiameter = diameter(root.left)
# 	rdiameter = diameter(root.right)

# 	return max(lheight + rheight + 1, max(ldiameter, rdiameter))


# if _name_ == "__main__":
	# """
	# Constructed binary tree is
	# 			1
	# 		/ \
	# 		2	 3
	# 	/ \
	# 	4	 5
	# """

	# root = Node(1)
	# root.left = Node(2)
	# root.right = Node(3)
	# root.left.left = Node(4)
	# root.left.right = Node(5)

	# # Function Call
	# print(diameter(root))


#tree class 4
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None

# def height(node):
#     if node is None:
#         return 0
#     left_height = height(node.left)
#     print(left_height)
#     right_height = height(node.right)
#     print(right_height)
#     sum = 1 + max(left_height, right_height)
#     return sum

# def diameter(root):
# 	if root is None:
# 		return 0
# 	lheight = height(root.left)
# 	print(lheight)
# 	rheight = height(root.right)
# 	print(rheight)
# 	ldiameter = diameter(root.left)
# 	print(ldiameter)
# 	rdiameter = diameter(root.right)
# 	print(ldiameter)

# 	return max(lheight + rheight + 1, max(ldiameter, rdiameter))

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# print("diamter = ",diameter(root))



#tree class 4

# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def isBalanced(root):
#     def checkHeight(node):
#         if not node:
#             return 0

#         left_height = checkHeight(node.left)
#         if left_height == -1:
#             return -1

#         right_height = checkHeight(node.right)
#         if right_height == -1:
#             return -1

#         if abs(left_height - right_height) > 1:
#             return -1

#         return max(left_height, right_height) + 1

#     # return checkHeight(root) != -1
#     if root.val !=-1:
#         return checkHeight(root) != None

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right = TreeNode(5)

# if isBalanced(root) == True:
#     print("tree is balanced")
# else:
#     print("tree is unbalamced")