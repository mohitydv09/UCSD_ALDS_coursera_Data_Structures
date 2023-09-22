# python3
from collections import deque

class q_stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.max1=[]
        self.max2=[]

    def enqueue(self,a):
        self.stack1.append(a)
        if not self.max1 or a >= self.max1[-1]:
            self.max1.append(a)
        
    def dequeue(self):
        #if empty
        if not self.stack2:
            #Jab tak Stack 1 bhara he
            self.max1=[]
            while self.stack1:
                val=self.stack1.pop()
                self.stack2.append(val)
                if not self.max2 or val >= self.max2[-1]:
                    self.max2.append(val)
                #If last element remove here only
                if len(self.stack1)==1:
                    self.stack1.pop()
            
        #else for Non-Empty
        else:
            val=self.stack2.pop()
            if self.max2 and val==self.max2[-1]:
                self.max2.pop()
        
    def Max(self):
        if self.max1 and self.max2:
            return max(self.max1[-1],self.max2[-1])
        elif self.max1 and not self.max2:
            return self.max1[-1]
        elif not self.max1 and self.max2:
            return self.max2[-1]


def max_sliding_window_naive(sequence, m):
    maximums = []
    # for i in range(len(sequence) - m + 1):
        # maximums.append(max(sequence[i:i + m]))
    for i in range(len(sequence)):
        answer.enqueue((sequence[i]))
        if i ==m-1:
            maximums.append(answer.Max())
        if i>=m:
            answer.dequeue()
            maximums.append(answer.Max())
        # print("Stack 1:",answer.stack1)
        # print("Max   1:",answer.max1)
        # print("Stack 2:",answer.stack2)
        # print("Max   2:",answer.max2)
        # print("------------------------")

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    # n=8
    # input_sequence=[2,7,3,1,5,2,6,2]
    assert len(input_sequence) == n
    window_size = int(input())
    # window_size=8
    answer=q_stack()
    print(*max_sliding_window_naive(input_sequence, window_size))

