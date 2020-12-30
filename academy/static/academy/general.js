document.addEventListener('DOMContentLoaded', () => {
    let alerts = document.querySelectorAll('.alert.alert-success, .alert.alert-warning');
    alerts.forEach(alert => {
        alert.addEventListener('animationend', () => {
            alert.style.display = 'none';
        })
    })
})