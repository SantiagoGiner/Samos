document.addEventListener('DOMContentLoaded', () => {
    let welcome = document.querySelector('#welcome');
    let background = document.querySelector('#background');
    let overview = document.querySelector('#overview');
    background.style.display = 'none';
    overview.style.display = 'none';
    welcome.addEventListener('animationend', () => {
        background.style.display = 'block';
    })
    background.addEventListener('animationend', () => {
        overview.style.display = 'block';
    })
})