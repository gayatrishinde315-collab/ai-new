from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))


def astar(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                new_pos = r * 3 + c

                new_state = list(state)

                new_state[zero], new_state[new_pos] = (
                    new_state[new_pos], new_state[zero])

                new_state = tuple(new_state)

                if new_state not in visited:
                    h = heuristic(new_state)

                    heappush(pq, (g + 1 + h, g + 1,
                                  new_state, path))

    return None


path = astar(start)

if path:
    print("Solution found:")

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Steps:", len(path) - 1)

else:
    print("No solution found")