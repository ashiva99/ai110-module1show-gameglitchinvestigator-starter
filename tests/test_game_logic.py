from logic_utils import check_guess, new_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_new_game_state_resets_session_fields():
    # A new game should always return the app to a playable state.
    state = new_game_state("Normal")

    assert state["status"] == "playing"
    assert state["attempts"] == 0
    assert state["history"] == []
    assert 1 <= state["secret"] <= 50


# --- Tests targeting the Normal/Hard range-swap bug and high/low hint bug ---

def test_normal_difficulty_range():
    # Bug: Normal was mapped to 1-100 instead of 1-50.
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 50), f"Normal should be 1-50, got {low}-{high}"


def test_hard_difficulty_range():
    # Bug: Hard was mapped to 1-50 instead of 1-100.
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 100), f"Hard should be 1-100, got {low}-{high}"


def test_easy_difficulty_range_unchanged():
    # Easy was never broken, but assert it stays correct as a regression guard.
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)


def test_check_guess_too_high_returns_correct_outcome():
    # Bug: hint direction was inverted — Too High was labelled "Go HIGHER!"
    # The outcome itself must be "Too High" when guess exceeds the secret.
    result = check_guess(75, 50)
    assert result == "Too High"


def test_check_guess_too_low_returns_correct_outcome():
    # Paired guard: Too Low must be "Too Low" when guess is below the secret.
    result = check_guess(25, 50)
    assert result == "Too Low"


def test_check_guess_with_string_secret():
    # Bug: on even attempts app.py cast secret to str; check_guess must still
    # compare numerically and not fall back to lexicographic string ordering.
    assert check_guess(5, "10") == "Too Low"   # "5" < "10" lexicographically, but 5 < 10 numerically
    assert check_guess(20, "10") == "Too High"
