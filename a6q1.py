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
