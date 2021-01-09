document.addEventListener('DOMContentLoaded', () => {
    const enrollForm = document.querySelector('#enroll');
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
    const exams = document.querySelectorAll(`#id_exam_1, #id_exam_2, #id_exam_3, #id_exam_4, #id_exam_5, 
                                             #id_exam_6, #id_exam_7, #id_exam_8, #id_exam_9, #id_exam_10`);
    exams.forEach(exam => {
        exam.onclick = () => {
            if (exam.checked) {
                document.querySelector('#id_test_date').required = true;
            }
            else {
                document.querySelector('#id_test_date').required = false;
            }
        }
    })
})