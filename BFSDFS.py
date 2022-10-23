# Problem 1

grid = []
file = open('input.txt', 'r')
for line in file.readlines():
    grid.append(line.strip().split(' '))

print('The input grid: ')
print(grid)

total_rows = len(grid)
total_cols = len(grid[0])

visited = [[False for y in range(total_cols)]
           for x in range(total_rows)]

dir_x = [+1, -1, 0, 0, +1, -1, +1, -1]
dir_y = [0, 0, +1, -1, +1, +1, -1, -1]


def is_out_of_bounds(r, c):
    if ((r < 0) or (r >= total_rows) or (c < 0) or (c >= total_cols)):
        return True
    return False


ans = 0
cnt = 0


def dfs(r, c):
    visited[r][c] = True
    global cnt
    cnt += 1
    for i in range(8):
        nr = r + dir_y[i]
        nc = c + dir_x[i]
        if (is_out_of_bounds(nr, nc)):
            continue
        if (visited[nr][nc]):
            continue
        if (grid[nr][nc] == 'N'):
            continue
        dfs(nr, nc)


for i in range(total_rows):
    for j in range(total_cols):
        if (grid[i][j] == 'N'):
            continue
        if (visited[i][j]):
            continue
        # global cnt
        cnt = 0
        dfs(i, j)
        ans = max(ans, cnt);

print('Answer:', ans)

#Problem2

grid = []
file = open('question2.txt', 'r')
total_rows = 0
total_cols = 0
INF = 200000000
cnt = 0
human_count = 0

dir_x = [+1, -1, 0, 0]
dir_y = [0, 0, +1, -1]


def is_out_of_bounds(r, c):
    if ((r < 0) or (r >= total_rows) or (c < 0) or (c >= total_cols)):
        return True
    return False


for line in file.readlines():
    global cnt
    cnt += 1
    if (cnt == 1):
        total_rows = int(line.strip())
    elif (cnt == 2):
        total_cols = int(line.strip())
    else:
        grid.append(line.strip().split(' '))

print('The input grid: ')
print(grid)

dist = [[INF for y in range(total_cols)]
        for x in range(total_rows)]

Q = []
for i in range(total_rows):
    for j in range(total_cols):
        if (grid[i][j] == 'A'):
            Q.append([i, j])
            dist[i][j] = 0
        if (grid[i][j] == 'H'):
            human_count += 1

# BFS
while len(Q) > 0:
    front = Q[0]
    Q.pop(0)
    r = front[0]
    c = front[1]
    for i in range(4):
        nr = r + dir_y[i]
        nc = c + dir_x[i]
        if (is_out_of_bounds(nr, nc)):
            continue
        if (dist[nr][nc] != INF):
            continue
        if ((grid[nr][nc] == 'A') or (grid[nr][nc] == 'T')):
            continue
        dist[nr][nc] = dist[r][c] + 1
        Q.append([nr, nc])

ans = 0
cnt = 0
for i in range(total_rows):
    for j in range(total_cols):
        if (dist[i][j] == INF):
            continue
        if (grid[i][j] == 'H'):
            cnt += 1
        ans = max(ans, dist[i][j])

print("Time:", ans, "minutes")
if (cnt == human_count):
    print('No one survived')
else:
    print((human_count) - cnt, 'survived')
