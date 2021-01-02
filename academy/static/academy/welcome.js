document.addEventListener('DOMContentLoaded', () => {
    let welcome = document.querySelector('#welcome');
    let background = document.querySelector('#background');
    background.style.display = 'none';
    welcome.addEventListener('animationend', () => {
        background.style.display = 'block';
    })
})