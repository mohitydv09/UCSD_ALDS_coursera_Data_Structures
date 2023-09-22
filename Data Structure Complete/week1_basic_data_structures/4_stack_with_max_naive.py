#python3
import sys
# import timedfg
# start=time.time()

class StackWithMax():
    i=0
    def __init__(self):
        self.__stack = []
        self.max_list=[]

    def Push(self, a):
        if StackWithMax.i==0:
            self.max_list.append(StackWithMax.i)
            self.__stack.append(a)
            StackWithMax.i+=1
            # print("Appended First:", a, "Max List Now:", self.max_list, "i:",StackWithMax.i)
        else:
            if a>self.__stack[self.max_list[-1]]:
                self.max_list.append(StackWithMax.i)
            else:
                self.max_list.append(self.max_list[-1])
            self.__stack.append(a)
            StackWithMax.i+=1
            # print("Appended:", a, "Max List Now:", self.max_list, "i:",StackWithMax.i)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.max_list.pop()
        StackWithMax.i-=1
        # print("Poped", "Max List Now:", self.max_list, "i:",StackWithMax.i)

    def Max(self):
        assert(len(self.__stack))
        return self.__stack[self.max_list[-1]]


if __name__ == '__main__':
    stack = StackWithMax()

    # with open("tests.txt","r") as f:
    #     num_queries=int(f.readline())
    #     for _ in range(num_queries):
    #         query = f.readline().split()
    #         # print(query)

    #         if query[0] == "push":
    #             stack.Push(int(query[1]))
    #         elif query[0] == "pop":
    #             stack.Pop()
    #         elif query[0] == "max":
    #             print(stack.Max())
    #         else:
    #             assert(0)

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
# end=time.time()
# print("time:",end-start)