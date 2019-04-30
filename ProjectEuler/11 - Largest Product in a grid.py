grid = []

for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
    
large = 0


# Horizental
for sub in grid:
    for n in range(17):
        p = sub[n] * sub[n+1] * sub[n+2] * sub[n+3]
        if  p> large:
            large = p

# Verticle
for a in range(20):
    for b in range(17):
        p = grid[b][a] * grid[b+1][a] * grid[b+2][a] * grid[b+3][a]
        if p>large:
            large = p

# Digonal
for a in range(17):
    for b in range(17):
        p = grid[a][b] * grid[a+1][b+1] * grid[a+2][b+2] * grid[a+3][b+3]
        if p > large:
            large = p


# Anti-Digonal
for a in range(17):
    for b in range(19,2,-1):
        p = grid[a][b] * grid[a+1][b-1] * grid[a+2][b-2] * grid[a+3][b-3]
        if p > large:
            large = p

print(large)