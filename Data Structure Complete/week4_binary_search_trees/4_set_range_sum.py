# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  """Updates the Sum of V node and set its as the parent of its children"""
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  """Does both Right or Left Rotation of Node V."""
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  # If V is the left child of its parent. Right Rotation is done here.
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  #Else if V is the right child of its parent. Left Rotation is happening here.
  else:
    m = v.left
    v.left = parent
    parent.right = m
  #Both parent and V are updated so that the sum is accurate and sets them as parent as there children
  update(parent)
  update(v)
  v.parent = grandparent
  #Set V as the child of the grandparent Now.
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  """Implement Zig, Zig-Zag or Zig- Zig rotations to perform splay."""
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig left Sided
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig right sided
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig will also be implemented by this as v.grandparent will be NONE
    # Zig will be implemented without any issue as the small rotation will take care if there is no grandparent
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes it the new root.
def splay(v):
  if v == None:
    return None
  # print("Splay ran on:",v.key)
  #Until v's parent exist
  while v.parent != None:
    # if no grandparent then do Small rotation
    if v.parent.parent == None:
      smallRotation(v)
      break
    # Otherwise do Big Rotation
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  # until root is not None
  while v != None:
    # this is done to keep track of the next element in the tree
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  # below if tree is null
  if result == None:    
    return (root, result)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  #Below line added
  left.parent=right
  update(right)
  return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)
  # root=splay(new_vertex)
  # splay(new_vertex)
  # print("After inserting:",x,"Root is:",root.key,"")
  # if root.left: print("Left:",root.left.key)
  # if root.right: print("Right:",root.right.key)
  # print("Left:",root.left.key,"Right:",root.right.key)

def erase(x): 
  # Wrong for test case 11
  global root
  # Implement erase yourself
  left,middle=split(root,x)
  middle,right=split(middle,x+1)
  root=merge(left,right)
  # next,root=find(root,x)
  # if next==None:
  #   return next
  # if next.key==x and next.right!=None:
  #   splay(next.right)
  #   # print("Root:",root.key,"Next:",next.key)
  #   l=root.left
  #   r=root.right
  #   r.left=l
  #   l.parent=r
  #   r.parent=None
  #   root=r
  #   update(l)
  #   update(root)
  # elif next.key==x and next.right==None:
  #   # print("Root;",root.key,"Root and next are same i.e. No Next element is there")
  #   l=next.left
  #   if l!=None: l.parent=None
  #   root=l
  #   update(root)
  # print("Removed:",x,"Root:",root.key)

def search(x): 
  global root
  # Implement find yourself
  next,root=find(root,x)
  if next!=None and next.key==x:
    return True
  return False
  

def sum(fr, to): 
  # Wrong for test case #10
  # print("Finding Sum betweem:",fr,to)
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  # ans=0
  # if middle!=None:
    # ans+=middle.sum
  # Complete the implementation of sum
  root=merge(merge(left,middle),right)
  if middle==None:
    # print("Last is None")
    return 0
  return middle.sum

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO