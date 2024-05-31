# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]
        # print("ran")


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        # self.elems=[]
        self.elems = [[] for _ in range(bucket_count)]
        # print(self.elems)

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        # print("hash generated for:",s, "Hash Is:",ans%self.bucket_count)
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        
        if query.type == "check":
            # hash_query=self._hash_func(query.s)
            my_list=[x for x in self.elems[query.ind]]
            self.write_chain(reversed(my_list))
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
                        # if self._hash_func(cur) == query.ind)
        else:
            # try:
            #     ind = self.elems.index(query.s)
            # except ValueError:
            #     ind = -1
            if query.type == 'find':
                hash_query=self._hash_func(query.s)
                self.write_search_result(query.s in self.elems[hash_query])
            elif query.type == 'add':
                hash_query=self._hash_func(query.s)
                if query.s not in self.elems[hash_query]:
                    self.elems[hash_query].append(query.s)
                # print("Elems:",self.elems)
                # if ind == -1:
                    # self.elems.append(query.s)
            else:
                hash_query=self._hash_func(query.s)
                for i,to_del in enumerate(self.elems[hash_query]):
                    if query.s == to_del:
                        self.elems[hash_query].pop(i)
                # if ind != -1:
                    # self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        # n=12
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    # bucket_count=int(5)
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
