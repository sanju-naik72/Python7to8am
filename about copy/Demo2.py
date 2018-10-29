import copy as cp
l1 = [10,20,30]
l2 = cp.copy(l1)
print(l1)
print(l2)
l2[1] = 90
print(l1)
print(l2)


