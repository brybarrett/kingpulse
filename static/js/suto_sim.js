document.addEventListener('DOMContentLoaded', () => {
  const tiltOptions = ['Low', 'Medium', 'High'];
  const clutchOptions = ['Low', 'Medium', 'High'];

  function getRandomLevel(options) {
    return options[Math.floor(Math.random() * options.length)];
  }

  function simulate() {
    const tilt = getRandomLevel(tiltOptions);
    const clutch = getRandomLevel(clutchOptions);

    updateTiltMeter(tilt);
    updateClutchMeter(clutch);

    const dangerBanner = document.getElementById('dangerBanner');
    if (tilt === 'High') {
      dangerBanner.classList.remove('hidden');
      dangerBanner.classList.add('flex');
    } else {
      dangerBanner.classList.add('hidden');
      dangerBanner.classList.remove('flex');
    }
  }

  // Start auto updates every 4 seconds
  setInterval(simulate, 4000);
});
