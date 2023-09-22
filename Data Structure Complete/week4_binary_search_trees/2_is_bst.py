#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
    return True
  result_list=[]
  result=inOrder(tree,0,result_list)
  # print(result)
  return all(a<=b for a,b in zip(result,result[1:]))

def inOrder(tree,root_index,result):

  i=root_index
  # print("Current Key:",tree[i][0])
  
  if tree[i][1]!=-1:
    inOrder(tree,tree[i][1],result)
  result.append(tree[i][0])
  if tree[i][2]!=-1:
    inOrder(tree,tree[i][2],result)
  return result

def main():
  nodes = int(sys.stdin.readline().strip())
  # tree = []
  global tree
  tree=[]
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
