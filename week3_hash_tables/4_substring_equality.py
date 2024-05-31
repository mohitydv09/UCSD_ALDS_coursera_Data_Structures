# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.multi=31
		self.h1=[0]
		self.h2=[0]
		self.prime1=1000000007
		self.prime2=1000000009
		self.multi_power1=[1]
		self.multi_power2=[1]

	def hash_gen(self):
		ele1,ele2=0,0

		for i in range(len(s)):
			ele1=(ele1*self.multi  +  ord(self.s[i]))%self.prime1
			ele2=(ele2*self.multi  +  ord(self.s[i]))%self.prime2
			self.h1.append(ele1)
			self.h2.append(ele2)
		# print("H1:",self.h1)
		# print("H2:",self.h2)

	def multi_power(self):
		x1=1
		x2=1
		for _ in range(len(self.s)):
			x1=(x1*self.multi)%self.prime1
			x2=(x2*self.multi)%self.prime2
			self.multi_power1.append(x1)
			self.multi_power2.append(x2)
		# print(self.multi_power1)
		# print(self.multi_power2)

	
	def ask(self, a, b, l):

		hash_a1=(self.h1[a+l]- (self.multi_power1[l]*self.h1[a])%self.prime1)%self.prime1
		hash_a2=(self.h2[a+l]- (self.multi_power2[l]*self.h2[a])%self.prime2)%self.prime2
		hash_b1=(self.h1[b+l]- (self.multi_power1[l]*self.h1[b])%self.prime1)%self.prime1
		hash_b2=(self.h2[b+l]- (self.multi_power2[l]*self.h2[b])%self.prime2)%self.prime2

		return hash_a1 == hash_b1 and hash_a2==hash_b2

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
solver.hash_gen()
solver.multi_power()
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
