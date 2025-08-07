// state_manager.js

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("matchup-form");
  const resultBox = document.getElementById("results");
  const commentaryBox = document.getElementById("commentary");
  const banner = document.getElementById("dangerBanner");
  const simCommentary = document.getElementById("simCommentary");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const teamA = document.getElementById("team-a").value;
    const teamB = document.getElementById("team-b").value;
    const scoreA = parseInt(document.getElementById("score-a").value);
    const scoreB = parseInt(document.getElementById("score-b").value);

    const payload = {
      team_a: teamA,
      team_b: teamB,
      score_a: scoreA,
      score_b: scoreB,
    };

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      // Update result box
      resultBox.innerHTML = `
        <p><strong>${teamA}:</strong> ${data.team_a_win_pct}%</p>
        <p><strong>${teamB}:</strong> ${data.team_b_win_pct}%</p>
        <p><strong>Tilt Level:</strong> ${data.tilt_level}</p>
        <p><strong>Clutch Rating:</strong> ${data.clutch_level}</p>
      `;

      // Update live commentary section
      commentaryBox.textContent = data.commentary;

      // Update meters
      updateTiltMeter(data.tilt_level);
      updateClutchMeter(data.clutch_level);

      // Update danger banner visibility
      if (data.tilt_level === "High") {
        banner.classList.remove("hidden");
        banner.classList.add("flex");
      } else {
        banner.classList.add("hidden");
        banner.classList.remove("flex");
      }
    } catch (error) {
      console.error("Analysis error:", error);
      resultBox.innerHTML = `<p style="color: red;">Something went wrong. Try again.</p>`;
      commentaryBox.textContent = "";
    }
  });
});
