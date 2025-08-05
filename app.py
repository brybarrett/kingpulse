from flask import Flask, render_template, request, jsonify
from pulse_engine import generate_commentary
from win_simulator import calculate_win_probability, get_tilt_level
import random
import os

app = Flask(__name__)

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
