"""
def sum_minor_diagonal(matrix):
    n = len(matrix)
    total = 0

    for i in range(n):
        j = n - 1 - i
        total += matrix[i][j]

    return total

# Test cases
matrix1 = [[1, -2, -3], [-4, 5, -6], [-7, -8, 9]]
matrix2 = [[3, 2], [2, 3]]

print(sum_minor_diagonal(matrix1))  # Output: -5
print(sum_minor_diagonal(matrix2))  # Output: 4

def binary(n):
    if n>1:
        binary(n//2)
        print(n%2,end="")
    num =int(input("num:"))
bin = binary(num)    
"""
