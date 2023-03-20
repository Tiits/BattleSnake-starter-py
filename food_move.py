from queue import Queue


# Use a breadth first algorithm to find the fastest path to the nearest food slot
def bfs_food(start, food, board_width, board_height, obstacles):
    # Set the variables
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    # Loop until the unvisited queue is empty
    while not frontier.empty():
        current = frontier.get()
        if current == food:
            # If we have reached the food break the loop
            break
        # Otherwise add the neighboring boxes to the unvisited queue
        for next in neighbors(current, board_width, board_height, obstacles):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    # Get the path back and reverse it to get the start move first
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    print(f"start: {start} et path 0: {path[0]}")
    return get_direction(start, path[0])

# Get the neighboring boxes
def neighbors(pos, board_width, board_height, obstacles):
    (x, y) = pos
    results = []
    if x > 0 and (x-1, y) not in obstacles:
        results.append((x-1, y))
    if x < board_width-1 and (x+1, y) not in obstacles:
        results.append((x+1, y))
    if y > 0 and (x, y-1) not in obstacles:
        results.append((x, y-1))
    if y < board_height-1 and (x, y+1) not in obstacles:
        results.append((x, y+1))
    return results

# Get the direction between two boxes
def get_direction(start, end):
    if start[0] < end[0]:
        return 'right'
    elif start[0] > end[0]:
        return 'left'
    elif start[1] < end[1]:
        return 'down'
    elif start[1] > end[1]:
        return 'up'
