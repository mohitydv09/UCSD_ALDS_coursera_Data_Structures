# python3

from collections import namedtuple
from collections import deque
import time


Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:
    current_time=0

    def __init__(self, size):
        self.size = size
        # self.finish_time = []
        self.finish_time=deque()

    def process(self, request):
        # write your code here
        #first addition to the buffer
        # print("Current Request:",request.arrived_at, request.time_to_process)

        if Buffer.current_time==0:
            self.finish_time.append(request.time_to_process+request.arrived_at)
            # print("Added first element to Q:",self.finish_time)
            Buffer.current_time=request.time_to_process+request.arrived_at
            # print("Current time after first ele:",Buffer.current_time)
            return Response(False,Buffer.current_time-request.time_to_process)
        
        #flush
        while request.arrived_at >= self.finish_time[0]:
            self.finish_time.popleft()
            # print("Flushed",self.finish_time)
            if not self.finish_time:
                break
        
        if len(self.finish_time)<self.size:
            self.finish_time.append(max(Buffer.current_time,request.arrived_at)+ request.time_to_process)
            Buffer.current_time=max(Buffer.current_time,request.arrived_at)+request.time_to_process
            # print("Current time Updated To:",Buffer.current_time)
            # print("Added at:",request.arrived_at,"List Now",self.finish_time)
            return Response(False, Buffer.current_time-request.time_to_process)
        else:
            return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    # with open('tests/03','r') as f:
        # buffer_size, n_requests = map(int, f.readline().split())
        # requests = []
        # for _ in range(n_requests):
        #     arrived_at, time_to_process = map(int, f.readline().split())
        #     requests.append(Request(arrived_at, time_to_process))
    # Printing input for surety
    # print('Buffer size:',buffer_size)
    # print('No of requests:',n_requests)
    # print('Requests:',requests)
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        # print("check")
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
