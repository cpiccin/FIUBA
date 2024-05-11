import logic


def main():
	grid = logic.initial_grid()
	turn = logic.PLAYERS[0]

	while True: # main game loop

		logic.show_grid(grid)

		mov = input('Enter coordinates. Column|Row: ')
		
		if mov in (logic.RESET, logic.RESET.lower()):
			turn = logic.PLAYERS[0]
			grid = logic.initial_grid()
			continue
		if mov in (logic.QUIT, logic.QUIT.lower()):
			break
		if mov.isnumeric() and len(mov) == 2:
			mov = (int(mov[0]), int(mov[1]))
		else:
			print('RESET, QUIT or enter valid coordinates. ')
			continue

		if logic.allowed_movement(mov, grid):
			grid = logic.modifies_grid(mov, grid, turn)
			if logic.game_won(grid, turn):
				logic.show_grid(grid)
				print(f'{turn} won!')
				return
			turn = logic.next_turn(turn)
		else:
			print('Outside grid limits. Enter another coordinate. ')
			continue


	print('Game Over')
	return

main()


