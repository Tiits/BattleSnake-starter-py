import typing
import random

# Setting basic information
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "Titouan",  # Our Battlesnake Username
        "color": "#1037e3",  # Our color
        "head": "all-seeing",  # Our head
        "tail": "mystic-moon",  # Our tail
    }


# Set if the game has started
def start(game_state: typing.Dict):
    print("GAME START")

# Set if the game has ended
def end(game_state: typing.Dict):
    print("GAME OVER\n")

# Function returning the movement of the snake
def move(game_state: typing.Dict) -> typing.Dict:
    from safe_moves import find_safe_moves
    from food_move import bfs_food

    # Define safe movements
    is_move_safe = find_safe_moves(game_state)
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)
    print(f"safe moves: {safe_moves}")

    # Go down if there is no safe move
    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")

        return {"move": "down", "shout": "No safe moves detected! Moving down!"}

    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)
    print(f"random move: {next_move}")

    # Find the move to get to the nearest food
    start_point = (game_state["you"]["body"][0]['x'], game_state["you"]["body"][0]['y'])
    food = game_state['board']['food']
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    obstacles = game_state['board']['snakes']
    food_move = bfs_food(start_point, food, board_width, board_height, obstacles)
    print(f"food_move: {food_move}")

    for move in safe_moves:
        if move == food_move:
            next_move = food_move
    print(f"next move after food move: {next_move}")

    if len(next_move) == 0:
        print(f"MOVE {game_state['turn']}: No next moves detected! Moving down")
        return {"move": "down", "shout": "No next moves detected! Moving down!"}

    return {"move": next_move, "shout": f"I will go {next_move}"}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
