document.addEventListener('DOMContentLoaded', () => {
    window.onscroll = () => {
        if  (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
            document.querySelector('html').style.backgroundImage = 'linear-gradient(45deg, #3c58b3 50%, #2a3c79 50%)';
            document.querySelector('body').style.backgroundImage = 'linear-gradient(45deg, #3c58b3 50%, #2a3c79 50%)';
        }
    }
})