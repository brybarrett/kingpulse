function checkDangerLevels() {
  const tiltLevel = document.getElementById('tiltLevel').value;
  const clutchLevel = document.getElementById('clutchLevel').value;

  const dangerBanner = document.getElementById('dangerBanner');

  if (
    (tiltLevel === 'High' && clutchLevel === 'High') ||
    (tiltLevel === 'Medium' && clutchLevel === 'High') ||
    (tiltLevel === 'High' && clutchLevel === 'Medium')
  ) {
    dangerBanner.classList.remove('hidden');
    dangerBanner.classList.add('flex');
    console.warn('[DANGER ALERT] Fantasy user may be tilting under pressure.');
  } else {
    dangerBanner.classList.remove('flex');
    dangerBanner.classList.add('hidden');
  }
}

// Run check after dropdown change
document.addEventListener('DOMContentLoaded', () => {
  const tiltSelect = document.getElementById('tiltLevel');
  const clutchSelect = document.getElementById('clutchLevel');

  if (tiltSelect && clutchSelect) {
    tiltSelect.addEventListener('change', checkDangerLevels);
    clutchSelect.addEventListener('change', checkDangerLevels);
  }
});
