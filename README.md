# 🧠 KingPulse – MVP Lite

Welcome to **KingPulse** — a real-time AI-powered momentum engine built as a proof of concept for the next evolution of fantasy sports inside **KingPool**.

This is a lean prototype designed to show how KingPool could integrate live-play analytics, emotional triggers, and AI-generated commentary to create an entirely new fantasy experience.

---

## 💡 Concept

**KingPulse** simulates what it would feel like if fantasy matchups had:
- Live win probability tracking
- Real-time emotional triggers (Tilt Meter, Choke Alerts, Comeback Mode)
- GPT-generated narrative commentary to drive engagement
- A momentum overlay that reacts to game flow — not just stats

> KingPool already owns pre-contest prep and post-contest content.
> KingPulse adds the heartbeat *during the contest* — where all the tension, trash talk, and emotional stickiness actually lives.

---

## 🛠️ What This MVP Includes

| Module | Functionality |
|--------|----------------|
| `win_simulator.py` | Basic fantasy matchup input and live win probability estimator |
| `pulse_engine.py` | GPT-driven narrative generator based on match state |
| `tilt_meter.js` | Visual Tilt Meter for emotional state (low, medium, high pressure) |
| `app.py` | Flask backend to glue it together |
| `templates/` | Frontend HTML UI with color-coded UX and results output |

---

## 🎯 Demo Use Case

1. Input 2 teams and their player scores
2. System estimates win probability for each side
3. GPT generates live trash talk / coaching comments based on the momentum swing
4. Tilt Meter updates with pressure level
5. Optional: Output card with shareable results

---

## 🧪 Tech Stack

- Python (Flask)
- OpenAI API (GPT-4)
- HTML/CSS (Tailwind-lite or custom)
- JS (for Tilt visuals)
- Optional: JSON test inputs or fake player data

---

## 📦 Goal

This MVP is not production-ready. It’s a **proof-of-vision** — built to show KingPool how one core feature could expand their platform’s engagement loop, deepen user retention, and give fantasy sports the adrenaline shot it’s been missing.

If you’re KingPool…  
Let’s build the full version *together*.

---

## 🧠 Author

**Bryan S. Barrett**  
AI Builder | DFS Engineer | Fantasy Systems Architect  
[Portfolio](https://bryansbarrett.dev) • [GitHub](https://github.com/yourusername) • [LinkedIn](https://www.linkedin.com/in/bryansbarrett)

---

> “Trash talk is better when it’s live.”
