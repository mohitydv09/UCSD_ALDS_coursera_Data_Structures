# python3


def build_heap(n,data,m):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # swaps = []
    global swaps
    swaps=[]
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps
    #find the length of the last top stack
    #start with the last element 
    for i in range(m,-1,-1):
        # print(i)
        # for all of them we need to call shiftdown
        shiftdown(i,data)
    return swaps
def shiftup():
    pass

def shiftdown(i,data):
    #i is the index from which shiftdown is to run
    #should check for minimum number and then swap,
    #after this go the the subtree which was swapped and do shiftdown again
    #check for two children
    # print("shiftdown was called for",i,data)
    n=len(data)
    child1_index=2*i+1
    child2_index=2*i+2
    if child1_index < n and child2_index < n:
        if data[child1_index]<data[child2_index] and data[i]>data[child1_index]:
            #swap 1 and parent
            data[i],data[child1_index]=data[child1_index],data[i]
            swaps.append((i,child1_index))
            # print("Swaped as child one was smaller than parent",data,i,child1_index)
            #now call shiftdown for the child which was swapped
            shiftdown(child1_index,data)
            
            # return i,child1_index
        elif data[child2_index]<data[child1_index] and data[i]>data[child2_index]:
            # swap 2 and parent
            data[i],data[child2_index]=data[child2_index],data[i]
            swaps.append((i,child2_index))
            # print("Swaped as child two was smaller than parent",data,i,child2_index)
            shiftdown(child2_index,data)
            # return i,child2_index
    elif child1_index < n and child2_index >= n:
        #check for only one parent shit
        #swap if the child is smaller
        if data[i]>data[child1_index]:
            data[i],data[child1_index]=data[child1_index],data[i]
            swaps.append((i,child1_index))
            # print("Swaped:",i,child1_index)
            # print(data)
            return i,child1_index
    else:
        #no Swaps nothin
        pass

def main():
    n = int(input())
    data = list(map(int, input().split()))
    # with open("tests/04","r") as f:
        # n=int(f.readline())
        # data = list(map(int,f.readline().split()))
    # n=10
    # data=[10,5,4,6,1,2,9,3,8,7]
    assert len(data) == n
    # print(n,data)
    # print(n.bit_length()-1)
    m=2**(n.bit_length()-1)-2
    # print("m:",m)
    swaps = build_heap(n,data,m)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
