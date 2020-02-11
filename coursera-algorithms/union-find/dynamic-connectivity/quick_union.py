
class QU():
    indices = []
    def __init__(self, N):
        self.N = N
        for index in range(N):
            self.indices.append(index)
    
    def __str__(self):
        return 'current index mapping: {}'.format(self.indices)

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.indices[i] = j

    def root(self, i):
        while self.indices[i] != i:
            i = self.indices[i]
        return i
        