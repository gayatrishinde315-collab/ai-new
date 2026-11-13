from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def bfs(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        path = path + [state]

        if state == goal:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for dr, dc in [(-1, 0), (1, 0),
                       (0, -1), (0, 1)]:

            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                pos = r * 3 + c

                new = list(state)
                new[zero], new[pos] = new[pos], new[zero]
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    queue.append((new, path))

    return None


path = bfs(start)

if path:
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Total steps:", len(path) - 1)

else:
    print("No solution found")