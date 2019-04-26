import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])

newmatrix = []
i = 0
while i < len(A):
    eachrow = [np.sum(A[i]*B[:,j]) for j in range(len(A))]
    i += 1
    newmatrix.append(eachrow)

print(np.array(newmatrix))


print(np.dot(A,B))
