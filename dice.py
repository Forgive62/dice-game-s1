from flask import Flask, jsonify
import random

app = Flask(__name__)

game_state = {
    "current_player": 1,
    "male": None
}

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

@app.route("/roll", methods=["GET"])
def roll():
    global game_state

    die1, die2 = roll_dice()
    total = die1 + die2
    current_player = game_state["current_player"]

    if game_state["male"] is None:  # First roll
        if total in [7, 11]:
            result = f"Pop! Player {current_player} wins immediately!"
            game_state["current_player"] = current_player  # Winner keeps dice
            game_state["male"] = None  # Reset game
        elif total in [2, 3, 12]:
            result = f"Craps! Player {current_player} loses immediately!"
            game_state["current_player"] = 3 - current_player  # Switch player
            game_state["male"] = None  # Reset game
        else:
            game_state["male"] = total
            result = f"The Male is {total}. Player {current_player} must roll it again."
    else:  # Subsequent rolls
        if total == game_state["male"]:
            result = f"Player {current_player} wins!"
            game_state["male"] = None  # Reset game
        elif total == 7:
            result = f"Player {current_player} loses! Player {3 - current_player} wins!"
            game_state["current_player"] = 3 - current_player  # Switch player
            game_state["male"] = None  # Reset game
        else:
            result = f"Player {current_player} rolled {total}. Roll again."

    return jsonify({
        "die1": die1,
        "die2": die2,
        "total": total,
        "result": result,
        "current_player": game_state["current_player"]
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
