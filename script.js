const ratingButtons = document.querySelectorAll('.rating-button');
const ratingTextarea = document.querySelector('.rating-textarea');

ratingButtons.forEach(button => {
  button.addEventListener('click', () => {
    ratingTextarea.value = `Em poucas palavras, descreva o que motivou a sua nota ${button.value}.`;
  });
});