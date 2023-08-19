#Name - Harry Patel
#NSID-ozc189
#Student Number-11358887
#Instructor-Lauressa Stilling
def initialRead_state(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    initialState = [list(line.strip()) for line in lines]
    return initialState
def neighboursCounting(grid_display, i, j):
    neighbours = []
    rows, cols = len(grid_display), len(grid_display[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        if 0 <= i + dx < rows and 0 <= j + dy < cols:
            neighbours.append(grid_display[i + dx][j + dy])
    return neighbours
def update_state(grid_display, previous_grid):
    new_grid_display = []
    for i, row in enumerate(grid_display):
        new_row = []
        for j, cell in enumerate(row):
            neighbours = neighboursCounting(grid_display, i, j)
            alive_neighbours = neighbours.count('*') + neighbours.count('Z')
            zombie_neighbours = neighbours.count('Z')

            # Handle living cells
            if cell == '*':
                # If a living cell has a zombie neighbour and that neighbour was a zombie in the previous iteration
                if zombie_neighbours > 0 and any([previous_grid[i + dx][j + dy] == 'Z' for dx, dy in
                                                  [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                                                  if 0 <= i + dx < len(grid_display) and 0 <= j + dy < len(
                            grid_display[0])]):
                    new_row.append('Z')
                elif alive_neighbours < 2 or alive_neighbours > 3:
                    new_row.append('-')
                else:
                    new_row.append('*')
            # Handle dead cells
            elif cell == '-':
                if alive_neighbours == 3:
                    new_row.append('Z')  # Cells that resurrect are Zombies
                else:
                    new_row.append('-')
            # Handle zombie cells
            elif cell == 'Z':
                if alive_neighbours == 2 or alive_neighbours == 3:
                    new_row.append('Z')
                else:
                    new_row.append('-')
        new_grid_display.append(new_row)
    return new_grid_display

