const toggleModal = () => {
  document.querySelector('.modal')
    .classList.toggle('modal--hidden');
  document.querySelector('.overlay')
    .classList.toggle('overlay--hidden');
}
document.querySelector('#show-modal')
  .addEventListener('click', toggleModal);

document.querySelector('.overlay')
  .addEventListener('click', toggleModal);

document.querySelector('#learn-more-form')
  .addEventListener('submit', (e) => {
  e.preventDefault();
  toggleModal();
});

document.querySelector('.modal__close-bar span')
  .addEventListener('click', toggleModal);
document.querySelector('.overlay')
  .addEventListener('click', toggleModal);
