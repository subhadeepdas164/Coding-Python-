import copy

class Mat:
    def __init__(self, A):
        self.nr = len(A)   #rows
        self.nc = len(A[0]) #columns
        self.data = copy.deepcopy(A)

    def mul(self, b):
        if self.nc == b.nr:
            A = []
            for i in range(self.nr):
                Ci = []
                for j in range(b.nc):
                    s = 0
                    for k in range(self.nc):
                        s += self.data[i][k] * b.data[k][j]
                    Ci.append(s)
                A.append(Ci)
            return Mat(A)
        else:
            print("Multiplication not possible")

    def display(self):
        for row in self.data:
            print(row)


A = [[1, 2, 3],[3, 5, 1]]

B = [[0, 1, 2, 3],[-1, 2, 0, 1],[9, 10, -1, 4]]

a = Mat(A)
b = Mat(B)

c = a.mul(b)

print("Result of Multiplication:")
c.display()
