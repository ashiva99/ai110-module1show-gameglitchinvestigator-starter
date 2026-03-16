import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        guess_num = int(guess)
        secret_num = int(secret)
    except (TypeError, ValueError):
        guess_str = str(guess)
        secret_str = str(secret)
        if guess_str == secret_str:
            return "Win"
        if guess_str > secret_str:
            return "Too High"
        return "Too Low"

    if guess_num == secret_num:
        return "Win"
    if guess_num > secret_num:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def new_game_state(difficulty: str) -> dict:
    """Return a fresh game state dict for the given difficulty."""
    import random
    low, high = get_range_for_difficulty(difficulty)
    return {
        "status": "playing",
        "attempts": 0,
        "score": 0,
        "history": [],
        "secret": random.randint(low, high),
    }


def new_game_state(difficulty: str):
    """Return a fresh session-state payload for a new game."""
    low, high = get_range_for_difficulty(difficulty)
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "status": "playing",
        "history": [],
    }
