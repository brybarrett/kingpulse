import random
# Uncomment if you're ready to use OpenAI API
# import openai
# import os
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Placeholder GPT fallback responses
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

def generate_commentary(team_a, team_b, score_a, score_b, a_win, b_win, tilt_level):
    # GPT-style prompt (only used if OpenAI is enabled)
    prompt = (
        f"Generate a 1-2 sentence live fantasy sports commentary based on this data:\n"
        f"Team A: {team_a}, Score: {score_a}, Win Probability: {a_win}%\n"
        f"Team B: {team_b}, Score: {score_b}, Win Probability: {b_win}%\n"
        f"Tilt Level: {tilt_level}\n"
        f"Make it clever, trash-talky, and emotional like a live sports announcer."
    )

    # Uncomment this block if using GPT-4:
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a fantasy sports announcer with sharp wit and ruthless energy."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.9
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"(GPT Fallback): {random.choice(fallback_comments.get(tilt_level, []))}"
    """

    # Fallback (static demo mode)
    return random.choice(fallback_comments.get(tilt_level, []))
