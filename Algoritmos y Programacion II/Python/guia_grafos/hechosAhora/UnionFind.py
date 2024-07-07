class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v, w):
        root_v = self.find(v)
        root_w = self.find(w)
        if root_v != root_w:
            if self.rank[root_v] < self.rank[root_w]:
                self.parent[root_v] = root_w
            elif self.rank[root_v] > self.rank[root_w]:
                self.parent[root_w] = root_v
            else:
                self.parent[root_w] = root_v
                self.rank[root_v] += 1