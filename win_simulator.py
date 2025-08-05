# win_simulator.py

def calculate_win_probability(team_a_score, team_b_score):
    """
    Estimate win probability based on raw score comparison.
    Returns (team_a_pct, team_b_pct) as rounded percentages.
    """
    total = team_a_score + team_b_score
    if total == 0:
        return 50.0, 50.0
    a_pct = round((team_a_score / total) * 100, 2)
    b_pct = round(100 - a_pct, 2)
    return a_pct, b_pct


def get_tilt_level(win_diff):
    """
    Determine emotional pressure level based on win % difference.
    Returns one of: 'Low', 'Medium', or 'High'.
    """
    if win_diff < 5:
        return "Low"
    elif win_diff < 15:
        return "Medium"
    else:
        return "High"
