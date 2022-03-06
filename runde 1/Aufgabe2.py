n = int(input())

import itertools
import collections


def isConnected(A: str, B: str, iA: int, iB: int) -> bool:
    return iA == iB or A == "M" or B == "M" or abs(iA-iB) == 1 or A == B

Q = set()


class ImmutableSet:
    def __init__(self, *items):
        self.underlying = set(items)
        self.hash = 0
        for e in items:
            self.hash ^= hash(e)

    def __iter__(self):
        return self.underlying

    def __contains__(self, e):
        return e in self.underlying

    def __eq__(self, other):
        return self.underlying == other.underlying

    def __hash__(self):
        return self.hash

    def __len__(self):
        return len(self.underlying)

    def __repr__(self):
        return f"ImmutableSet({self.underlying})"


for a, b, c in itertools.permutations(
    set(itertools.product({"A", "B", "C"}, range(1, n+1))) | {("M", 0)},
    r=3
):
    if isConnected(a[0], b[0], a[1], b[1]) and isConnected(a[0], c[0], a[1], c[1]) and isConnected(b[0], c[0], b[1], c[1]):
        Q.add(ImmutableSet(a, b, c))


print(len(Q))
# print(Q)

