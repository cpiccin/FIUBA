PLAYERS = ['X', 'O', '$', '#'] 
DIM = 5
RESET = 'R'
QUIT = 'Q'
EMPTY = ' '

def initial_grid():
	grid = []
	for i in range(DIM):
		col = []
		for j in range(DIM):
			col += [EMPTY]
		grid.append(col)
	return grid


def allowed_movement(mov, grid): # x = col, y = row
	x, y = mov[0], mov[1]
	if x < 0 or y < 0:
		return False
	if x >= DIM or y >= DIM:
		return False
	if grid[y][x] == EMPTY: # movement is allowed
		return True
	if grid[y][x] in PLAYERS:
		return False


def modifies_grid(mov, grid, turn):
	new_grid = []
	for i in grid:
		new_grid.append(i)
	x, y = mov[0], mov[1]
	new_grid[y][x] = turn 
	return new_grid


def next_turn(turn):
	n = PLAYERS.index(turn)
	if (n + 1) >= len(PLAYERS):
		return PLAYERS[0]
	else:
		return PLAYERS[n+1]


def show_grid(grid):
	for n in range(DIM+1):
		if n == 0:
			print(' ', end='  ')
		else:
			print(n-1, end='  ')
	print()
	n = 0
	for i in grid:
		print(n, end='  ')
		for c in i:
			print(c, end='  ')
		print()
		n += 1


def game_won(grid, turn):
	aux = 0
	cant = 0
	for i in range(DIM):
		for j in range(DIM):
			if grid[i][j] == turn:
				cant += 1
			if aux == DIM:
				return True
			if turn == grid[i][j]:
				aux += 1
		if cant == 2:
			return False
		cant = 0  
	if aux == DIM:
		return True
	else:
		return False

