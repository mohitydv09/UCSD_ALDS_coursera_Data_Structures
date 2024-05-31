# python3

import sys
from collections import defaultdict

debug=False
class Hashtable:
    def __init__(self,t,p):
        self.t=t
        self.p=p
        self.prime1=1000000007
        self.prime2=1000000009
        self.x=31
        self.x_power1=[1]
        self.x_power2=[1]
        self.hashes_t1=[0]
        self.hashes_t2=[0]
        self.hashes_p1=[0]
        self.hashes_p2=[0]
        
    def poly_hash_gen(self):
        """To generate hashes for a given string"""
        ele1,ele2=0,0
        for i in range(len(self.t)):
            ele1=(ele1*self.x  +  ord(self.t[i]))%self.prime1
            ele2=(ele2*self.x  +  ord(self.t[i]))%self.prime2
            self.hashes_t1.append(ele1)
            self.hashes_t2.append(ele2)
        
        ele1,ele2=0,0
        for i in range(len(self.p)):
            ele1=(ele1*self.x  +  ord(self.p[i]))%self.prime1
            ele2=(ele2*self.x  +  ord(self.p[i]))%self.prime2
            self.hashes_p1.append(ele1)
            self.hashes_p2.append(ele2)

        if debug: print("T1:",self.hashes_t1)
        if debug: print("T2:",self.hashes_t2)
        if debug: print("P1:",self.hashes_p1)
        if debug: print("P1:",self.hashes_p2)
        
    def x_power_gen(self):
        x1=1
        x2=1
        for _ in range(min(len(t),len(p))):
            x1=(x1*self.x)%self.prime1
            x2=(x2*self.x)%self.prime2
            self.x_power1.append(x1)
            self.x_power2.append(x2)
        if debug: print('X Powers 1:',self.x_power1)
        if debug: print('X Powers 2:',self.x_power2)
        
    # def poly_hash(self,start,end,st)
    #     how=(self.hashes_t1[end_t]- (self.x_power1[(end_t-st)//2]*self.hashes_t1[st])%self.prime1)%self.prime1
    #     return 
    
    def next_mismatch(self,st,end_t,sp,end_p):
        if debug: print("Ram Next Mismatch")
        if debug: print("st,sp,endt,endp:",st,sp,end_t,end_p)
        mid_t=(st+end_t+1)//2
        mid_p=(sp+end_p+1)//2
        if debug: print("MID:",mid_t,mid_p)
        if debug: print("tmid:",self.t[st:mid_t],self.t[st:mid_t+1])
        if debug: print("pmid:",self.p[sp:mid_p],self.p[sp:mid_p+1])
        #To handle the end cases where only two letter string is present
        if end_t-st==1:
            #first is same
            if self.t[st]==self.p[sp]:
                #last is also same
                if self.t[end_t]==self.t[end_p]:
                    if debug: print("both are same returned:",-1,-1)
                    return -1,-1
                # only first letter is same
                else:
                    if debug: print("last element is diff, retruned:",end_t,end_p)
                    return end_t,end_p
            else:
                if debug: print("Both ele are diff, returned:",st,sp)
                return st,sp
        if end_t==st:
            #only one ele
            if self.t[st]==self.p[sp]:
                return -1,-1
            else:
                return end_t,end_p
        # mid_t=(st+end_t+1)//2
        # mid_p=(sp+end_p+1)//2
        # print("MID:",mid_t,mid_p)
        # print("tmid:",self.t[st:mid_t],self.t[st:mid_t+1])
        # print("pmid:",self.p[sp:mid_p],self.p[sp:mid_p+1])
        hash_t1_mid= (self.hashes_t1[mid_t]- (self.x_power1[mid_t-st]*self.hashes_t1[st])%self.prime1)%self.prime1
        hash_t2_mid= (self.hashes_t2[mid_t]- (self.x_power2[mid_t-st]*self.hashes_t2[st])%self.prime2)%self.prime2
        hash_t1_mid1=(self.hashes_t1[mid_t+1]- (self.x_power1[mid_t-st+1]*self.hashes_t1[st])%self.prime1)%self.prime1
        hash_t2_mid1=(self.hashes_t2[mid_t+1]- (self.x_power2[mid_t-st+1]*self.hashes_t2[st])%self.prime2)%self.prime2
        hash_p1_mid= (self.hashes_p1[mid_p]- (self.x_power1[mid_p-sp]*self.hashes_p1[sp])%self.prime1)%self.prime1
        hash_p2_mid= (self.hashes_p2[mid_p]- (self.x_power2[mid_p-sp]*self.hashes_p2[sp])%self.prime2)%self.prime2
        hash_p1_mid1=(self.hashes_p1[mid_p+1]- (self.x_power1[mid_p-sp+1]*self.hashes_p1[sp])%self.prime1)%self.prime1
        hash_p2_mid1=(self.hashes_p2[mid_p+1]- (self.x_power2[mid_p-sp+1]*self.hashes_p2[sp])%self.prime2)%self.prime2
    
        if debug: print(hash_t1_mid,hash_p1_mid)
        is_mid_same=(hash_t1_mid==hash_p1_mid and hash_t2_mid==hash_p2_mid)
        is_mid1_same=(hash_t1_mid1==hash_p1_mid1 and hash_t2_mid1==hash_p2_mid1)
        if debug: print(is_mid_same,is_mid1_same)
        
        #To handle the end cases where only two letter string is present
        # if end_t-st<=1:
        #     #first is same
        #     if self.t[st]==self.p[sp]:
        #         #last is also same
        #         if self.t[end_t]==self.t[end_p]:
        #             return -1,-1
        #         # only first letter is same
        #         else:
        #             return end_t,end_p
        #     else:
        #         return st,sp
        # Handle case when first element is wrong
        # if mid_t==st:
        #     print("First ele is wrong returned:",st,sp)
        #     return st,sp
        # # Handle case when strings are same
        # if st+1==end_t:
        #     print("Strings are same, returned:",-1,-1)
        #     return -1,-1
        #binary serach implementation
        if is_mid_same:
            if not is_mid1_same:
                #Found Mismatch
                if debug: print("Found Mismatch")
                if debug: print("Returned",mid_t,mid_p)
                return mid_t,mid_p
            else:
                #Go aage
                return self.next_mismatch(mid_t,end_t,mid_p,end_p)
        else:
            #Cut in Half
            return self.next_mismatch(st,mid_t,sp,mid_p)



    def is_present(self,st,et,sp,ep,k):
        if debug: print("Ran Is Present for:")
        if debug: print("st,end_t,sp,end_p:",st, sp,et,ep)
        start_t=st
        start_p=sp
        end_t=et
        end_p=ep
        # i=0
        # while i<k:
        for _ in range(k):
            mm_index_t,mm_index_p=self.next_mismatch(start_t,end_t,start_p,end_p)
            if mm_index_t==-1 or mm_index_t==end_t:
                if debug: print("returned:",True)
                return True
            start_t=mm_index_t+1
            start_p=mm_index_p+1
            # i+=1
        mm_index_t,mm_index_p=self.next_mismatch(start_t,end_t,start_p,end_p)
        if mm_index_t==-1:
            if debug: print("Further string is equal")
            return True
        if debug: print("returned:",False)
        return False
    
    def solve(self,k):
        if debug: print("Ran Solve")
        positions=[]
        for i in range(len(self.t)-len(self.p)+1):
            if debug: print("ran ran for i:",i)
            # print("Is Present:",self.is_present(i,i+len(self.p)-1,0,len(self.p)-1,k))
            if self.is_present(i,i+len(self.p)-1,0,len(self.p)-1,k):
                positions.append(i)
        return positions

for line in sys.stdin.readlines():
    k, t, p = line.split()
    hashtable=Hashtable(t,p)
    hashtable.x_power_gen()
    hashtable.poly_hash_gen()
    ans=hashtable.solve(int(k))
    # ans = solve(int(k), t, p)
    print(len(ans), *ans)

# with open("test.txt",'r') as f:
#     xx=f.readlines()
#     for line in xx:
#         k,t,p=line.split()
#         print("K:",k)
#         print("T:",t)
#         print("P:",p)
#         hashtable=Hashtable(t,p)
#         hashtable.x_power_gen()
#         hashtable.poly_hash_gen()
#         print(hashtable.solve(int(k)))