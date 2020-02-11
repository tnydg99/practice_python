
class QUv2():
    indices = []
    size = []
    def __init__(self, N):
        self.N = N
        for index in range(N):
            self.indices.append(index)
            self.size.append(1)
    
    def __str__(self):
        return 'current index mapping: {}\ncurrent size mapping: {}\n'.format(self.indices, self.size)

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        elif self.size[i] < self.size[j]:
            self.indices[i] = j
            self.size[j] += self.size[i]
        else:
            self.indices[j] = i
            self.size[i] += self.size[j]

    def root(self, i):
        while self.indices[i] != i:
            self.indices[i] = self.indices[self.indices[i]]
            i = self.indices[i]
        return i
        