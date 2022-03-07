import itertools

while True:
    n = int(input("N: "))

    G = set()
    D = set()


    def connected(a, b):
        if (a[0] == "M" or b[0] == "M"):
            return True

        if (abs(a[1] - b[1]) <= 1):
            return True

        return False

    def on_one_line(a, b, c):
        if len({a[0], b[0], c[0]} - {"M"}) == 1:
            return True

        x, y, z = sorted((a[1], b[1], c[1]))
        if (x == y == z - 1):
            return True

        return False


    vertices = {("M", 0)}

    for i in range(1, n + 1):
        for c in ("A", "B", "C"):
            vertices.add((c, i))

    for a, b in itertools.combinations(vertices, 2):
        if connected(a, b):
            G.add((min(a, b, key=lambda e: e[1]), max(a, b, key=lambda e: e[1])))

    for a, b, c in itertools.combinations(vertices, 3):
        if on_one_line(a, b, c):
            continue

        a, b, c = sorted((a, b, c), key=lambda e: e[1])
        D.add((a, b, c))

    print(len(D))
