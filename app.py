from flask import Flask, render_template, request, jsonify
from pulse_engine import generate_commentary
import random
import os

app = Flask(__name__)

# --- Utility Functions ---

def calculate_win_probability(team_a_score, team_b_score):
    total = team_a_score + team_b_score
    if total == 0:
        return 50, 50
    a_pct = round((team_a_score / total) * 100, 2)
    b_pct = round(100 - a_pct, 2)
    return a_pct, b_pct

def get_tilt_level(win_diff):
    if win_diff < 5:
        return "Low"
    elif win_diff < 15:
        return "Medium"
    else:
        return "High"

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    team_a = data.get('team_a')
    team_b = data.get('team_b')
    score_a = int(data.get('score_a', 0))
    score_b = int(data.get('score_b', 0))

    a_win, b_win = calculate_win_probability(score_a, score_b)
    win_diff = abs(a_win - b_win)
    tilt = get_tilt_level(win_diff)

    commentary = generate_commentary(team_a, team_b, score_a, score_b, a_win, b_win, tilt)

    result = {
        "team_a_win_pct": a_win,
        "team_b_win_pct": b_win,
        "tilt_level": tilt,
        "commentary": commentary
    }

    return jsonify(result)

# --- Run Server ---

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
