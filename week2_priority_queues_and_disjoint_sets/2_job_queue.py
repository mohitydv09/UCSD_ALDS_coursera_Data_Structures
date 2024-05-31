# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def buildheap(n):
    """This funtion initializes the heap as a array with two items in it."""
    heap=[[0,i] for i in range(n)]
    return heap
    

def change_p(heap,val):
    """Increase the val of element by the amount of time the next element will take."""
    heap[0][0]+=val
    shiftdown(0,heap)
    

def shiftdown(i,data):
    n=len(data)
    child1_index=2*i+1
    child2_index=2*i+2
    if child1_index < n and child2_index < n:
        if data[child1_index][0]<data[child2_index][0] and data[i][0]>data[child1_index][0]:
            data[i],data[child1_index]=data[child1_index],data[i]
            # swaps.append((i,child1_index))
            # print("Swaped as child one was smaller than parent",data,i,child1_index)
            shiftdown(child1_index,data)
        elif data[child1_index][0]<data[child2_index][0] and data[i][0]==data[child1_index][0]:
            if data[i][1]>data[child1_index][1]:
                data[i],data[child1_index]=data[child1_index],data[i]
                # swaps.append((i,child1_index))
                # print("Swaped as child one was smaller than parent",data,i,child1_index)
                shiftdown(child1_index,data)

        elif data[child2_index][0]<data[child1_index][0] and data[i][0]>data[child2_index][0]:
            data[i],data[child2_index]=data[child2_index],data[i]
            # swaps.append((i,child2_index))
            # print("Swaped as child two was smaller than parent",data,i,child2_index)
            shiftdown(child2_index,data)

        elif data[child2_index][0]<data[child1_index][0] and data[i][0]==data[child2_index][0]:
            if data[i][1]>data[child2_index][1]:
                data[i],data[child2_index]=data[child2_index],data[i]
                # swaps.append((i,child2_index))
                #print("Swaped as child two was smaller than parent",data,i,child2_index)
                shiftdown(child2_index,data)
        elif data[child2_index][0]==data[child1_index][0] and data[i][0]>data[child2_index][0]:
            if data[child2_index][1]>data[child1_index][1]:
                data[i],data[child1_index]=data[child1_index],data[i]
                shiftdown(child1_index,data)

            else:
                data[i],data[child2_index]=data[child2_index],data[i]
                shiftdown(child2_index,data)
        elif data[child2_index][0]==data[child1_index][0] and data[i][0]==data[child2_index][0]:
            if data[child1_index][1]>data[child2_index][1] and data[i][0]>data[child2_index][1]:
                data[i],data[child2_index]=data[child2_index],data[i]
                shiftdown(child2_index,data)
            elif data[child1_index][1]<data[child2_index][1] and data[i][0]>data[child1_index][1]:
                data[i],data[child1_index]=data[child1_index],data[i]
                shiftdown(child1_index,data)

    elif child1_index < n and child2_index >= n:
        if data[i][0]>data[child1_index][0]:
            data[i],data[child1_index]=data[child1_index],data[i]

        elif data[i][0]==data[child1_index][0]:
            if data[i][1] > data[child1_index][1]:
                data[i],data[child1_index]=data[child1_index],data[i]


def assign_jobs(n_workers, jobs,heap):
    # TODO: replace this code with a faster algorithm.
    result = []
    for job in jobs:
        next_worker=heap[0][1]
        result.append(AssignedJob(next_worker, heap[0][0]))
        change_p(heap,job)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    # with open("tests/02","r") as f:
        # n_workers,n_jobs=map(int,f.readline().split())
        # jobs=list(map(int,f.readline().split()))

    assert len(jobs) == n_jobs
    heap=buildheap(n_workers)
    assigned_jobs = assign_jobs(n_workers, jobs,heap)

    for job in assigned_jobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()
