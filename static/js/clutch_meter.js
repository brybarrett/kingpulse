function updateClutchMeter(clutchLevel) {
  const meter = document.getElementById('clutchVisual');
  const icon = document.getElementById('clutchIcon');
  const label = document.getElementById('clutchLabel');

  let color, width, symbol, message;

  switch (clutchLevel) {
    case 'Low':
      color = 'bg-gray-400';
      width = 'w-1/3';
      symbol = '';
      message = 'Missed Opportunity';
      break;
    case 'Medium':
      color = 'bg-blue-400';
      width = 'w-2/3';
      symbol = '';
      message = 'Solid Play';
      break;
    case 'High':
      color = 'bg-green-500';
      width = 'w-full';
      symbol = '';
      message = 'Ice In The Veins';
      break;
    default:
      color = 'bg-gray-500';
      width = 'w-1/6';
      symbol = '';
      message = 'Waiting...';
  }

  meter.className = `h-4 rounded transition-all duration-500 ${color} ${width}`;
  icon.innerText = symbol;
  label.innerText = message;
}
