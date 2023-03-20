
def find_safe_moves(game_state):
    # Safe move dictionary
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # Set the variables
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    my_head = game_state["you"]["body"][0]
    my_neck = game_state["you"]["body"][1]
    my_body = game_state['you']['body']
    opponents = game_state['board']['snakes']

    # Avoid turning back
    if my_neck["x"] < my_head["x"]:
        is_move_safe["left"] = False
    elif my_neck["x"] > my_head["x"]:
        is_move_safe["right"] = False
    elif my_neck["y"] < my_head["y"]:
        is_move_safe["down"] = False
    elif my_neck["y"] > my_head["y"]:
        is_move_safe["up"] = False

    # Avoid map borders
    if my_head["x"] == 0:
        is_move_safe["left"] = False
    elif my_head["x"] == board_width - 1:
        is_move_safe["right"] = False

    if my_head["y"] == 0:
        is_move_safe["down"] = False
    elif my_head["y"] == board_height - 1:
        is_move_safe["up"] = False

    # Avoid our own body
    for body in my_body:
        if body["x"] == my_head["x"] + 1 and body["y"] == my_head["y"]:
            is_move_safe["right"] = False
        elif body["x"] == my_head["x"] - 1 and body["y"] == my_head["y"]:
            is_move_safe["left"] = False

        if body["y"] == my_head["y"] + 1 and body["x"] == my_head["x"]:
            is_move_safe["up"] = False
        elif body["y"] == my_head["y"] - 1 and body["x"] == my_head["x"]:
            is_move_safe["down"] = False

    # Avoid opponents
    for opponent in opponents:
        for opponent_body in opponent["body"]:
            if opponent_body["x"] == my_head["x"] + 1 and opponent_body["y"] == my_head["y"]:
                is_move_safe["right"] = False
            elif opponent_body["x"] == my_head["x"] - 1 and opponent_body["y"] == my_head["y"]:
                is_move_safe["left"] = False

            if opponent_body["y"] == my_head["y"] + 1 and opponent_body["x"] == my_head["x"]:
                is_move_safe["up"] = False
            elif opponent_body["y"] == my_head["y"] - 1 and opponent_body["x"] == my_head["x"]:
                is_move_safe["down"] = False

    return is_move_safe
