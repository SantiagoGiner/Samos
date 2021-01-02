document.addEventListener('DOMContentLoaded', () => {
    let enrollForm = document.querySelector('#enroll');
    enrollForm.style.display = 'none';
    document.querySelectorAll('.modal-footer > .btn.btn-success').forEach(button => {
        button.onclick = () => {
            enrollForm.style.display = 'block';
            enrollForm.scrollIntoView();
        }
    })
    document.querySelector('#close').onclick = () => {
        enrollForm.style.display = 'none';
    }
})