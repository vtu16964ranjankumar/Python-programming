'''loop statement
'''
# s=input("Enter the string:")
# for i in s:
#   print(i)

"""Nested Loop to print the matrix;
"""
print("Method 1 to use for loop")
matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
for i in range(0,3):
  for j in range(0,3):
    print(matrix[i][j],end=" ")
  print()

print("Method 2 to use for loop")
for i in matrix: #here i and j is not indices, but themseleves a element
  for j in i:
    print(j,end=" ")
  print()

""" To command over loops in python solve the star pattern question """