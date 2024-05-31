# python3

import sys
import threading

class node:
    def __init__(self,val) -> None:
        self.val=val
        self.childs=[]
    
    def add_child(self,child):
        self.childs.append(child)
    
    def __repr__(self) -> str:
        return f"Node({self.val},{[x.val for x in self.childs]} children)"

def compute_height(start_node):
    if not start_node.childs:
        return 1
    else:
        return 1 + max(compute_height(x) for x in start_node.childs)

def main():
    # n = int(input())
    # parents = list(map(int, input().split()))
    with open("tests/15") as f:
        n=int(f.readline())
        parents=list(map(int,f.readline().split()))

    nodes=[node(x) for x in range(n)]

    for i in range(n):
        if parents[i]==-1:
            root=nodes[i]
        else:
            nodes[parents[i]].add_child(nodes[i])

    for i in range(n):
        print(nodes[i])
    print(compute_height(root))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
