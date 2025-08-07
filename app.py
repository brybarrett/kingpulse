from flask import Flask, render_template, request, jsonify, send_from_directory
from pulse_engine import generate_commentary
from win_simulator import calculate_win_probability, get_tilt_level
import random
import os

app = Flask(__name__)

# --- Static File Fix ---
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

# --- Home Route ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Analyze Simulation POST Route ---
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    team_a = data.get('team_a')
    team_b = data.get('team_b')
    score_a = int(data.get('score_a', 0))
    score_b = int(data.get('score_b', 0))

    # Win % + Tilt Logic
    a_win, b_win = calculate_win_probability(score_a, score_b)
    win_diff = abs(a_win - b_win)
    tilt = get_tilt_level(win_diff)

    # Mock Clutch Logic
    clutch_level = random.choice(["Low", "Medium", "High"])

    # Commentary Generation
    commentary = generate_commentary(team_a, team_b, score_a, score_b, a_win, b_win, tilt)

    # MUST include raw data back to frontend
    result = {
        "team_a": team_a,
        "team_b": team_b,
        "score_a": score_a,
        "score_b": score_b,
        "team_a_win_pct": a_win,
        "team_b_win_pct": b_win,
        "tilt_level": tilt,
        "clutch_level": clutch_level,
        "commentary": commentary
    }

    return jsonify(result)

# --- Run Local Server ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
