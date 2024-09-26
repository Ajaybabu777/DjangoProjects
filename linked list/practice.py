# class node:
#     def __init__(self,item):
#         self.item = item
#         self.left = None
#         self.right = None

# # def preorder(root):
# #     if root is not None:
# #         print(root.item)
# #         preorder(root.left)
# #         preorder(root.right)

# # def inorder(root):
# #     if root is not None:
# #         inorder(root.left)
# #         print(root.item)
# #         inorder(root.right)

# def postorder(root):
#     if root is not None:
#          postorder(root.left)
#          postorder(root.right)
#          print(root.item)

# rootnode=node(1)
# rootnode.left=node(2)
# rootnode.right=node(3)
# rootnode.left.left=node(5)
# rootnode.left.right=node(4)
# rootnode.right.right=node(8)

# # preorder(rootnode)
# # inorder(rootnode)
# postorder(rootnode)



class Treenode:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None


def lot(root):
    if not root:
        print("tree is empty")

    else:
        que=[]
        que.append(root)

        while que:
            node=que.pop(0)
            print(node.val)

            if node.left:
                que.append(node.left)
            
            if node.right:
                que.append(node.right)



root=Treenode("warangal")
root.left=Treenode("karimnagar")
root.left.left=Treenode("vijayawada")
root.left.right=Treenode("secundrabad")
root.right=Treenode("nagole")

lot(root)