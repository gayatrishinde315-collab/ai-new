def dfs(a, b, visited):

    if (a, b) in visited:
        return False

    print(a, b)
    visited.add((a, b))

    if a == 2 or b == 2:
        print("Goal reached!")
        return True

    moves = [
        (4, b),
        (a, 3),
        (0, b),
        (a, 0),

        (a - min(a, 3-b), b + min(a, 3-b)),

        (a + min(b, 4-a), b - min(b, 4-a))
    ]

    for x, y in moves:
        if dfs(x, y, visited):
            return True

    return False


dfs(0, 0, set())