import math

class matrix():


    def __init__(self, arr):
        self.arr = arr
        self.col = len(arr[0])
        self.row = len(arr)


    def __add__(self, other):
        self.sum=[]
        for i in range(self.row):
            r=[]
            for j in range(self.col):
                r.append(self.arr[i][j] + other.arr[i][j])
            self.sum.append(r)
        return matrix(self.sum)


    def __sub__(self,other):
        self.sub=[]
        for i in range(self.row):
            r=[]
            for j in range(self.col):
                r.append(self.arr[i][j] - other.arr[i][j])
            self.sub.append(r)
        return matrix(self.sub)


    def __mul__(self, other):
        c=[]
        for i in range(self.row):
            another_line = []
            for j in range(other.col):
                another_line.append(0)
            c.append(another_line)

        for w in range(self.row):
            for j in range(other.col):
                s = 0
                for i in range(other.row):
                    s += self.arr[w][i] * other.arr[i][j]
                c[w][j] = s
        c = matrix(c)
        return c


    def __str__(self):
        return '\n'.join([f'{i}' for i in self.arr])

a = matrix([[1,2],
            [3,4]])

print(a*a)