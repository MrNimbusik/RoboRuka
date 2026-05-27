const button = document.getElementById('toggleBtn');
const statusText = document.getElementById('statusText');

let enabled = false;

button.addEventListener('click', () => {

  enabled = !enabled;

  document.body.classList.toggle('active');

  if (enabled) {

    button.textContent = 'ON';
    button.classList.remove('off');
    button.classList.add('on');

    statusText.textContent = 'ON';
    statusText.classList.remove('off-text');
    statusText.classList.add('on-text');

  } else {

    button.textContent = 'OFF';
    button.classList.remove('on');
    button.classList.add('off');

    statusText.textContent = 'OFF';
    statusText.classList.remove('on-text');
    statusText.classList.add('off-text');

  }

});