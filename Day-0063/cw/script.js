let score = 0;
let pointsPerClick = 1;

const scoreElement = document.getElementById('score');
const pointsPerClickElement = document.getElementById('pointsPerClick');
const cookieElement = document.getElementById('cookie');


cookieElement.addEventListener('click', () => {
  score += pointsPerClick;
  scoreElement.textContent = score;
  pointsPerClick = Math.pow(2, Math.floor(score / 100));
  pointsPerClickElement.textContent = pointsPerClick;
  cookieElement.classList.add('shake');
  setTimeout(() => {
    cookieElement.classList.remove('shake');
  }, 200);
});
