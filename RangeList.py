#Python program to generate lists using range() functions

#List A
A = []
for i in range(45, 60+1, 1):
    if i%2 == 0:
        A.append(i)
print("List A: ", A)

#List B
B = []
for j in range(60, 80+1, 1):
    if j%2 != 0:
        B.append(j)
print("List B ", B)
print()
print("Length of A: ", len(A))
print("Length of B: ", len(B))
