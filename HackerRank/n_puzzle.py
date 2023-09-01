from collections import deque

def main():
    X = int(input())
    problem = []
    for _ in range(X * X):
        t = int(input())
        problem.append(t)

    Y = X
    m = {}
    prev = {}
    q = deque()
    v = list(range(X * Y))
    m[tuple(v)] = (0, 0)
    prev[tuple(v)] = (v, "")
    q.append(v)
   
    while q:
        v = q.popleft()
        coor, x, y = m[tuple(v)][0], m[tuple(v)][0] % X, m[tuple(v)][0] // X
        depth = m[tuple(v)][1]
        next_v = v[:]
       
        if 0 < x:
            v[coor], v[coor - 1] = v[coor - 1], v[coor]
            if tuple(v) not in m:
                m[tuple(v)] = (coor - 1, depth + 1)
                q.append(v[:])
                prev[tuple(v)] = (next_v, "RIGHT")
            v[coor], v[coor - 1] = v[coor - 1], v[coor]
       
        if x < X - 1:
            v[coor], v[coor + 1] = v[coor + 1], v[coor]
            if tuple(v) not in m:
                m[tuple(v)] = (coor + 1, depth + 1)
                q.append(v[:])
                prev[tuple(v)] = (next_v, "LEFT")
            v[coor], v[coor + 1] = v[coor + 1], v[coor]
       
        if 0 < y:
            v[coor], v[coor - X] = v[coor - X], v[coor]
            if tuple(v) not in m:
                m[tuple(v)] = (coor - X, depth + 1)
                q.append(v[:])
                prev[tuple(v)] = (next_v, "DOWN")
            v[coor], v[coor - X] = v[coor - X], v[coor]
       
        if y < Y - 1:
            v[coor], v[coor + X] = v[coor + X], v[coor]
            if tuple(v) not in m:
                m[tuple(v)] = (coor + X, depth + 1)
                q.append(v[:])
                prev[tuple(v)] = (next_v, "UP")
            v[coor], v[coor + X] = v[coor + X], v[coor]
       
        if tuple(problem) in m:
            break
   
    print(m[tuple(problem)][1])
    while tuple(prev[tuple(problem)][0]) != tuple(problem):
        print(prev[tuple(problem)][1])
        problem = list(prev[tuple(problem)][0])

if __name__ == "__main__":
    main()
