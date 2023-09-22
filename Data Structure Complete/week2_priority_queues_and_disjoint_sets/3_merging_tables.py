# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        # print("Merge ran for src, dst:",src,dst)
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        src_rank=self.ranks[src_parent]
        dst_rank=self.ranks[dst_parent]

        if src_parent == dst_parent:
            #means they are already in same set therefore nothing needs to be done
            # print("Parents are same")
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        # Get ranks of both the trees

        if src_rank>dst_rank:
            self.parents[dst_parent]=self.parents[src_parent]
            if src_rank==dst_rank:
                #change the rank of the parent of source
                self.ranks[src_parent]+=1
            self.row_counts[src_parent]+=self.row_counts[dst_parent]
            if self.row_counts[src_parent]>self.max_row_count:
                self.max_row_count=self.row_counts[src_parent]
            self.row_counts[dst_parent]=0
            # self.max_row_count = max(self.row_counts)
        else:
            self.parents[src_parent]=self.parents[dst_parent]
            if src_rank==dst_rank:
                self.ranks[dst_parent]+=1
            self.row_counts[dst_parent]+=self.row_counts[src_parent]
            self.row_counts[src_parent]=0
            if self.row_counts[dst_parent]>self.max_row_count:
                self.max_row_count=self.row_counts[dst_parent]
            # self.max_row_count = max(self.row_counts)
            
        # print("ranks  :",self.ranks)
        # print("Parents:",self.parents)
        # print("Counts :",self.row_counts)
        return True

    def get_parent(self, table):
        # find parent and compress path
        # print("table:",table,self.parents[table])
        if self.parents[table]!=table:
            # table=self.parents[table]
            # self.get_parent(table)
            self.parents[table]=self.get_parent(self.parents[table])
            # print("parent finding")
        # print("parent of given item is:",table)
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    # n_tables, n_queries = 5,5
    counts = list(map(int, input().split()))
    # counts=[1,1,1,1,1]
    assert len(counts) == n_tables
    db = Database(counts)
    # inp=[3,5,2,4,1,4,5,4,5,3]
    for i in range(n_queries):
        dst, src = map(int, input().split())
        # dst,src=inp[i],inp[i+1]
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)
        # print(max(db.row_counts))


if __name__ == "__main__":
    main()
