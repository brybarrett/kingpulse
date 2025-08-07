import random
import json
import os

# Uncomment below to enable GPT mode
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Commentary by Tilt Level ---
fallback_comments = {
    "Low": [
        "Neck and neck! This one's going down to the wire.",
        "You couldn’t ask for a tighter matchup — every point counts.",
        "Tensions are rising but no one’s folding yet."
    ],
    "Medium": [
        "You’re starting to pull ahead, but don’t let your guard down.",
        "Momentum is shifting... who’s got the clutch gene?",
        "It’s getting spicy — somebody's about to tilt."
    ],
    "High": [
        "Absolute meltdown in progress. This is fantasy carnage.",
        "You're steamrolling them. Should we call the fantasy coroner?",
        "Choke alert activated. This comeback story’s about to get ugly."
    ]
}

# --- Win % Calculation ---
def calculate_win_probability(score_a, score_b):
    total = score_a + score_b
    if total == 0:
        return 50, 50
    a_pct = round((score_a / total) * 100, 2)
    b_pct = round(100 - a_pct, 2)
    return a_pct, b_pct

# --- Tilt Level Classification ---
def get_tilt_level(win_diff):
    if win_diff < 5:
        return "Low"
    elif win_diff < 15:
        return "Medium"
    else:
        return "High"

# --- Commentary Engine (Fallback or GPT) ---
def generate_commentary(team_a, team_b, score_a, score_b, a_win, b_win, tilt_level):
    prompt = (
        f"Generate a 1-2 sentence live fantasy sports commentary based on this data:\n"
        f"Team A: {team_a}, Score: {score_a}, Win Probability: {a_win}%\n"
        f"Team B: {team_b}, Score: {score_b}, Win Probability: {b_win}%\n"
        f"Tilt Level: {tilt_level}\n"
        f"Make it clever, trash-talky, and emotional like a live sports announcer."
    )

    # GPT-4 Mode (optional)
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a fantasy sports announcer with sharp wit and ruthless energy."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=60,
            temperature=0.9
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"(GPT Fallback): {random.choice(fallback_comments.get(tilt_level, []))}"
    """

    # Fallback commentary
    return random.choice(fallback_comments.get(tilt_level, ["No commentary available."]))

# --- Batch Simulation (All Events) ---
def run_simulations():
    path = os.path.join("static", "assets", "events.json")
    try:
        with open(path, "r") as f:
            events = json.load(f)
    except Exception as e:
        return [{"error": "Failed to load events.json"}]

    results = []
    for event in events:
        team_a = event["team_a"]
        team_b = event["team_b"]
        score_a = int(event["score_a"])
        score_b = int(event["score_b"])

        a_win, b_win = calculate_win_probability(score_a, score_b)
        tilt = get_tilt_level(abs(a_win - b_win))
        commentary = generate_commentary(team_a, team_b, score_a, score_b, a_win, b_win, tilt)

        results.append({
            "team_a": team_a,
            "team_b": team_b,
            "score_a": score_a,
            "score_b": score_b,
            "team_a_win_pct": a_win,
            "team_b_win_pct": b_win,
            "tilt_level": tilt,
            "commentary": commentary
        })

    return results
