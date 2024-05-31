# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def __init__(self):
    self.result_in_order=[]
    self.result_pre_order=[]
    self.result_post_order=[]
    
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,root_index):

    # Finish the implementation
    # You may need to add a new recursive method to do that
    i=root_index
    # print("Current Key:",self.key[i])
    
    if self.left[i]!=-1:
      self.inOrder(self.left[i])
    self.result_in_order.append(self.key[i])
    if self.right[i]!=-1:
      self.inOrder(self.right[i])
    
    return self.result_in_order

  def preOrder(self,root_index):
    
    # Finish the implementation
    # You may need to add a new recursive method to do that
    i=root_index
    # print("Current Key:",self.key[i])
    self.result_pre_order.append(self.key[i])
    if self.left[i]!=-1:
      self.preOrder(self.left[i])
    if self.right[i]!=-1:
      self.preOrder(self.right[i])
    
    return self.result_pre_order

  def postOrder(self,root_index):

    # Finish the implementation
    # You may need to add a new recursive method to do that
    i=root_index
    # print("Current Key:",self.key[i])

    if self.left[i]!=-1:
      self.postOrder(self.left[i])
    if self.right[i]!=-1:
      self.postOrder(self.right[i])
    self.result_post_order.append(self.key[i])
    return self.result_post_order

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder(0)))
	print(" ".join(str(x) for x in tree.preOrder(0)))
	print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()
