# python3

import sys
from collections import defaultdict


debug=False
class Hashtable:
    def __init__(self,s,t):
        self.s=s
        self.t=t
        self.prime1=1000000007
        self.prime2=1000000009
        self.x=31
        self.x_power1=[1]
        self.x_power2=[1]
        self.hashes_s1=[0]
        self.hashes_s2=[0]
        self.hashes_t1=[0]
        self.hashes_t2=[0]
        
    def poly_hash_gen(self):
        """To generate hashes for a given string"""
        ele1,ele2=0,0
        for i in range(len(self.s)):
            ele1=(ele1*self.x  +  ord(self.s[i]))%self.prime1
            ele2=(ele2*self.x  +  ord(self.s[i]))%self.prime2
            self.hashes_s1.append(ele1)
            self.hashes_s2.append(ele2)
        
        ele1,ele2=0,0
        for i in range(len(self.t)):
            ele1=(ele1*self.x  +  ord(self.t[i]))%self.prime1
            ele2=(ele2*self.x  +  ord(self.t[i]))%self.prime2
            self.hashes_t1.append(ele1)
            self.hashes_t2.append(ele2)

        if debug: print("S1:",self.hashes_s1)
        if debug: print("S2:",self.hashes_s2)
        if debug: print("T1:",self.hashes_t1)
        if debug: print("T1:",self.hashes_t2)
        
    def x_power_gen(self):
        x1=1
        x2=1
        for _ in range(min(len(s),len(t))):
            x1=(x1*self.x)%self.prime1
            x2=(x2*self.x)%self.prime2
            self.x_power1.append(x1)
            self.x_power2.append(x2)
        if debug: print('X Powers 1:',self.x_power1)
        if debug: print('X Powers 2:',self.x_power2)
        
    def linear_hash(self,num):
        a=43
        b=243
        l_hash=(((a*num)+b)%self.prime1)
        return  l_hash

    def check_k(self,k):
        """To check if there is a equal substring of length k<min(s,t)"""
        # IN this funtion we need S to be the larger string
        substring_hashes1=defaultdict(lambda:-1)
        substring_hashes2=defaultdict(lambda:-1)
        for i in range(len(self.s)-k+1):
            hash_s1=(self.hashes_s1[i+k]- (self.x_power1[k]*self.hashes_s1[i])%self.prime1)%self.prime1
            hash_s2=(self.hashes_s2[i+k]- (self.x_power2[k]*self.hashes_s2[i])%self.prime2)%self.prime2
            hash_hash_s1=self.linear_hash(hash_s1)
            hash_hash_s2=self.linear_hash(hash_s2)
            substring_hashes1[hash_hash_s1]=i
            substring_hashes2[hash_hash_s2]=i
        # print("Substring Hashes:",substring_hashes1)
        # print("Substring Hashes:",substring_hashes2)
        # print("Default Check:", substring_hashes1['Hello'] )

        for i in range(len(self.t)-k+1):
            hash_t1=(self.hashes_t1[i+k]- (self.x_power1[k]*self.hashes_t1[i])%self.prime1)%self.prime1
            hash_t2=(self.hashes_t2[i+k]- (self.x_power2[k]*self.hashes_t2[i])%self.prime2)%self.prime2
            hash_hash_t1=self.linear_hash(hash_t1)
            hash_hash_t2=self.linear_hash(hash_t2)
            if substring_hashes1[hash_hash_t1]!=-1 and substring_hashes2[hash_hash_t2]!=-1:
                return substring_hashes1[hash_hash_t1],i,k
        return 0,0,0

        
    def solve(self,start,end):
        mid=(start+end)//2
        # print("Solve ran with mid:",mid,start,end)
        
        if start==min(len(self.s),len(self.t))-1:
            return hashtable.check_k(mid+1)
        if mid==0:
            return hashtable.check_k(1)
        if hashtable.check_k(mid)[2]!=0 and hashtable.check_k(mid+1)[2]==0:
            # print("Found ans with mid:",mid)
            return hashtable.check_k(mid)
        elif hashtable.check_k(mid)[2]!=0 and hashtable.check_k(mid+1)[2]!=0:
            # print("Aage jana he")
            return self.solve(mid,end)
        elif hashtable.check_k(mid)[2]==0:
            # print("Mid m jana he")
            return self.solve(start,mid)
            
        # for k in range(small,0,-1):
        #     # print("K:",k)
        #     if hashtable.check_k(k)!=False:
        #         # ans = Answer(hashtable.check_k(k))
        #         ans=hashtable.check_k(k)
        #         # print("Ans:",ans)
        #         return ans
        # return 0,0,0

            
    # def binary_solve(self,k)
    


for line in sys.stdin.readlines():
    s, t = line.split()
    hashtable=Hashtable(s,t)
    hashtable.x_power_gen()
    hashtable.poly_hash_gen()
    ans = hashtable.solve(0,min(len(s),len(t)))
    print(*ans)


# with open("test.txt",'r') as f:
#     xx=f.readlines()
#     for line in xx:
#         s,t=line.split()
#         print("S:",s)
#         print("T:",t)
#         hashtable=Hashtable(s,t)
#         hashtable.x_power_gen()
#         hashtable.poly_hash_gen()
#         # print(hashtable.check_k(3))
#         ans=hashtable.solve(0,min(len(s),len(t)))
#         print(*ans)