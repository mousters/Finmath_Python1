class Matrix():

    def __init__(self, listnumbers):
    # Constructor
        self.listnumbers = listnumbers


    def __repr__(self):
    # You will certainly need to overload this operator
        return str('\n'.join(str(e).replace('[', '').replace(']', '').replace(',', '') for e in self.listnumbers))

    def getTranspose(self):
    # You will create the function transpose
        r = len(self.listnumbers)
        c = len(self.listnumbers[0])
        trans_mat = []
        for i in range(c):
            trans_mat.append([row[i] for row in self.listnumbers])
        transpose_mat = Matrix(trans_mat)
        return transpose_mat


    def getDimension(self):
    # You will create the function getDimension which returns number of rows and number of columns
        rows = len(self.listnumbers)
        columns = len(self.listnumbers[0])
        return rows, columns


    def __eq__(self, mat):
    # You need to be able to show that 2 matrices are equal
        if (self.listnumbers == mat):
            return True
        else:
            return False


    def __add__(self, mat):
    # You need to be able to make an addition between 2 matrices
        r = len(self.listnumbers)
        c = len(self.listnumbers[0])
        sum_mat = []
        for i in range(r):
            row = []
        for j in range(c):
            row.append(self.listnumbers[i][j] + mat.listnumbers[i][j])
            sum_mat.append(row)
        summed_mat = Matrix(sum_mat)
        return summed_mat


    def __mul__(self, mat):
    # You need to multiply two matrices
        r = len(self.listnumbers)
        c = len(mat.listnumbers[0])
        mult_mat = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                for k in range(len(mat.listnumbers)):
                    mult_mat[i][j] += self.listnumbers[i][k]*mat.listnumbers[k][j]
                    multiply_mat = Matrix(mult_mat)

        return mult_mat
if __name__=='__main__':
    mat=Matrix([[1,2,3],[4,5,6]])
    mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(mat==mat2)
    print(mat.getTranspose())
    print(mat.__add__(mat2))
    print(mat.__mul__(mat2))
