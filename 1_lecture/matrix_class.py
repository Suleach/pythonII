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
        for i in range(len(self.arr)):
            another_line = []
            for j in range(len(other.arr[0])):
                another_line.append(0)
            c.append(another_line)

        for w in range(len(self.arr)):
            for j in range(len(other.arr[0])):
                s = 0
                for i in range(len(other.arr)):
                    s += self.arr[w][i] * other.arr[i][j]
                c[w][j] = s
        c = matrix(c)
        return c


    def __str__(self):
        return str(self.arr)

a = matrix([[1,2],
            [3,4]])

print(a*a)