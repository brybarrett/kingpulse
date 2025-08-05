function updateTiltMeter(tiltLevel) {
  const meter = document.getElementById('tiltVisual');
  const icon = document.getElementById('tiltIcon');
  const label = document.getElementById('tiltLabel');

  let colorClass, widthClass, emoji, message;

  switch (tiltLevel) {
    case 'Low':
      colorClass = 'bg-green-400';
      widthClass = 'w-1/3';
      emoji = '😐';
      message = 'Calm & Collected';
      break;
    case 'Medium':
      colorClass = 'bg-yellow-400';
      widthClass = 'w-2/3';
      emoji = '😠';
      message = 'Getting Heated';
      break;
    case 'High':
      colorClass = 'bg-red-500 animate-pulse';
      widthClass = 'w-full';
      emoji = '💀';
      message = 'Full Tilt Meltdown';
      break;
    default:
      colorClass = 'bg-gray-500';
      widthClass = 'w-1/6';
      emoji = '🤖';
      message = 'Unknown';
  }

  // Apply styles
  meter.className = `h-4 rounded transition-all duration-500 ${colorClass} ${widthClass}`;
  icon.innerText = emoji;
  label.innerText = message;
}
