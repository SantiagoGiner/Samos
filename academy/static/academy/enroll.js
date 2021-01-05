document.addEventListener('DOMContentLoaded', () => {
    let enrollForm = document.querySelector('#enroll');
    enrollForm.style.display = 'none';
    document.querySelectorAll('.modal-footer > .btn.btn-success').forEach(button => {
        button.onclick = () => {
            window.setTimeout(() => {
                enrollForm.style.display = 'block';
                enrollForm.scrollIntoView({block: 'start', behavior: 'smooth'});
                enrollForm.scroll(0, 0);
            },
            500)
        }
    })
    document.querySelector('#close').onclick = () => {
        enrollForm.style.display = 'none';
    }
})