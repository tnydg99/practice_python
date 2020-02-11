
class QF():
    indices = []
    def __init__(self, N):
        self.N = N
        for index in range(N):
            self.indices.append(index)
    
    def __str__(self):
        return 'current index mapping: {}'.format(self.indices)

    def connected(self, p, q):
        return self.indices[p] == self.indices[q]

    def union(self, p, q):
        connected_nodes = [index for index, value in enumerate(self.indices) 
                          if self.indices[index] == self.indices[p]]
        for index in connected_nodes:
            self.indices[index] = self.indices[q]
        