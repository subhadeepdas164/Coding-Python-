class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        result = []
        for i in range(len(self.matrix[0])):
            row = []
            for j in range(len(self.matrix)):
                row.append(self.matrix[j][i])
            result.append(row)
        return result


m = Matrix([[1, 2, 3],
            [4, 5, 6]])

print("Transpose:")
for row in m.transpose():
    print(row)
