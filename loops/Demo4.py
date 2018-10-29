
for x in "sathya":
    print(x)

for x in "sathya":
    print(x,end=" ")
print("Thanks")

# using Slice Operator on String
s1 = "Sathya"
for x in s1[0:6:2]:
    print(x)
print("Thanks")


for x in s1[::-1]:
    print(x)


print("---------------------------")

# Example Programs on nested loop's

# WAP to Display
#  1 2 3
#  1 2 3
#  1 2 3

for y in range(3):# outer loop
    for x in range(1,4):  # inner loop
        print(x,end=" ")
    print()
print("-----------------------")
# WAP to Display
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5

for y in range(5):
    for x in range(1,6):
        print(x,end=" ")
    print()

print("-----------------------")
# WAP to Display
#  3 2 1
#  3 2 1
#  3 2 1

for y in range(3):
    for x in range(3,0,-1):
        print(x,end=" ")
    print()

