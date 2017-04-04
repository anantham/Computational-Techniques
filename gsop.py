#Gram-Schmidt process

import numpy as np

def innerProduct(p,q):
	return np.dot(p,q)

def GramSchmidt(B):
	Q = []
	n = len(B)
	for i, b in enumerate(B):
		componentToRemove = np.zeros(n)
		for j in range(0,i):
			componentToRemove += innerProduct(Q[j],b)*Q[j]
			print Q[j]
			print componentToRemove
		q = b - componentToRemove
		norm = np.linalg.norm(q)
		Q.append(map(lambda x: x/norm, q))
	return Q

print "Enter the dimension of the vector space"
n = raw_input()

B = []
print "\nNow enter the Basis vector's elements seperated by spaces\n"

for i in range(int(n)):
	print str(i+1)+"th Basis vector"
	temp = raw_input()
	B.append(np.array(map(int,temp.split(" "))))

print B

Q = GramSchmidt(B)

print "\n The orthogonal basis for the vector space spanned by the above basis is "
print Q