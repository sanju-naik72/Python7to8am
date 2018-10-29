
import copy as cp

l1 = [[10,20,30],[40,50,60],[70,80]]
l2 = cp.deepcopy(l1)

print(l1)
print(l2)

l1[1][1] = "Sathya"

print(l1)
print(l2)
