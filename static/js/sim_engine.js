document.addEventListener('DOMContentLoaded', () => {
  let simInterval = null;

  const toggleButton = document.getElementById('autoToggle');
  const simButton = document.getElementById('startSimButton');
  const tiltBar = document.getElementById('tiltBar');
  const clutchBar = document.getElementById('clutchBar');
  const tiltLabel = document.getElementById('tiltLabel');
  const clutchLabel = document.getElementById('clutchLabel');
  const commentaryBox = document.getElementById('commentaryBox');
  const dangerBanner = document.getElementById('dangerBanner');

  // Fallback: If no span structure exists for matchups
  const teamA = document.getElementById('teamA') || document.createElement('span');
  const teamB = document.getElementById('teamB') || document.createElement('span');
  const teamAScore = document.getElementById('teamAScore') || document.createElement('span');
  const teamBScore = document.getElementById('teamBScore') || document.createElement('span');

  let eventData = [];

  async function loadEvents() {
    try {
      const res = await fetch('/assets/events.json');
      eventData = await res.json();
      console.log("[📦] Events loaded:", eventData.length);
    } catch (err) {
      console.error("[❌] Failed to load events.json:", err);
    }
  }

  function getRandomEvent() {
    const index = Math.floor(Math.random() * eventData.length);
    return eventData[index];
  }

  async function simulate() {
    if (eventData.length === 0) {
      console.warn("[⚠️] No events to simulate.");
      return;
    }

    const event = getRandomEvent();

    try {
      const res = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event)
      });

      const result = await res.json();

      // Update meters
      tiltLabel.textContent = result.tilt_level;
      clutchLabel.textContent = result.clutch_level;

      const tiltIndex = ["Low", "Medium", "High"].indexOf(result.tilt_level);
      const clutchIndex = ["Low", "Medium", "High"].indexOf(result.clutch_level);
      tiltBar.value = tiltIndex >= 0 ? tiltIndex + 1 : 0;
      clutchBar.value = clutchIndex >= 0 ? clutchIndex + 1 : 0;

      // Danger banner
      if (result.tilt_level === "High") {
        dangerBanner.classList.remove("hidden");
        dangerBanner.classList.add("flex");
      } else {
        dangerBanner.classList.add("hidden");
        dangerBanner.classList.remove("flex");
      }

      // Matchup display fallback (if needed)
      const matchupDisplay = document.getElementById('matchupDisplay');
      if (matchupDisplay) {
        matchupDisplay.innerHTML = `
          <span class="font-semibold text-gray-800 dark:text-gray-100" id="teamA">${event.team_a}</span>
          <span class="text-gray-600 dark:text-gray-300" id="teamAScore">(${event.score_a})</span>
          <span class="text-gray-500 mx-2">vs</span>
          <span class="font-semibold text-gray-800 dark:text-gray-100" id="teamB">${event.team_b}</span>
          <span class="text-gray-600 dark:text-gray-300" id="teamBScore">(${event.score_b})</span>
        `;
      }

      // Commentary
      commentaryBox.textContent = result.commentary;

      console.log("[🎯] Simulated:", event.team_a, "vs", event.team_b);

    } catch (err) {
      console.error("[💥] Simulation error:", err);
    }
  }

  // Manual Sim
  simButton.addEventListener('click', simulate);

  // Auto Sim Toggle
  toggleButton.addEventListener('click', () => {
    const isOn = toggleButton.textContent === "ON";

    if (isOn) {
      toggleButton.textContent = "OFF";
      toggleButton.classList.remove('text-green-700', 'border-green-700', 'bg-green-50');
      toggleButton.classList.add('text-gray-600', 'border-gray-400');
      clearInterval(simInterval);
    } else {
      toggleButton.textContent = "ON";
      toggleButton.classList.remove('text-gray-600', 'border-gray-400');
      toggleButton.classList.add('text-green-700', 'border-green-700', 'bg-green-50');
      simInterval = setInterval(simulate, 4000);
    }
  });

  // Theme toggle fallback
  const themeToggle = document.getElementById("themeToggle");
  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      document.documentElement.classList.toggle("dark");
    });
  }

  loadEvents();
});
