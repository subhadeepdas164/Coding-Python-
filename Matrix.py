class Matrix:
    def __init__(self, data):
        """Initializes the Matrix object with nested list data."""
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        """Provides a string representation for the print function."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    def transpose(self):
        """Returns the transpose of the matrix."""
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)

    def multiply(self, other_matrix):
        """
        Multiplies this matrix by another Matrix object.
        Multiplication is only possible if the number of columns in the 
        first matrix equals the number of rows in the second matrix.
        """
        if self.cols != other_matrix.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second.")

        # Initialize the result matrix with zeros
        result_data = [[0 for _ in range(other_matrix.cols)] for _ in range(self.rows)]

        # Perform the matrix multiplication using nested loops
        for i in range(self.rows): # Iterate through rows of Matrix A
            for j in range(other_matrix.cols): # Iterate through columns of Matrix B
                for k in range(self.cols): # Iterate through rows of Matrix B (or columns of A)
                    result_data[i][j] += self.data[i][k] * other_matrix.data[k][j]

        return Matrix(result_data) # Return a new Matrix object with the result

# --- Example Usage ---
# Define two matrices as nested lists
# Matrix A (2x3)
A_data = [
    [1, 2, 3],
    [4, 5, 6]
]
# Matrix B (3x2) - The number of rows (3) matches A's columns (3)
B_data = [
    [7, 8],
    [9, 1],
    [2, 3]
]

# Create Matrix objects
mat_a = Matrix(A_data)
mat_b = Matrix(B_data)

print(f"Matrix A (dimensions {mat_a.rows}x{mat_a.cols}):\n{mat_a}")
print(f"Matrix B (dimensions {mat_b.rows}x{mat_b.cols}):\n{mat_b}")

# Multiply the matrices
try:
    mat_c = mat_a.multiply(mat_b)
    print(f" \n Result of A * B (dimensions {mat_c.rows}x{mat_c.cols}): \n {mat_c}")
except ValueError as e:
    print(f"Error: {e}")


print(f"\nTranspose of Matrix A:\n{mat_a.transpose()}")
