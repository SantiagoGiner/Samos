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
    const disableSubjects = document.querySelector('#id_subjects_6');
    const disableExams = document.querySelector('#id_exam_11');
    const subjects = document.querySelectorAll(
        '#id_subjects_1, #id_subjects_2, #id_subjects_3, #id_subjects_4, #id_subjects_5');
    const exams = document.querySelectorAll(
        '#id_exam_1,#id_exam_2,#id_exam_3,#id_exam_4,#id_exam_5,#id_exam_6,#id_exam_7,#id_exam_8,#id_exam_9, #id_exam_10')
    const testDate = document.querySelector('#div_id_test_date');
    disableSubjects.onclick = () => {
        if (disableSubjects.checked) {
            subjects.forEach(option => {
                option.disabled = true;
            }) 
            testDate.style.display = 'block';
            document.querySelector('#id_test_date').required = true;
        }
        else {
            subjects.forEach(option => {
                option.disabled = false;
            })
            testDate.style.display = 'none';
            document.querySelector('#id_test_date').required = false;
        }
    }
    disableExams.onclick = () => {
        if (disableExams.checked) {
            exams.forEach(option => {
                option.disabled = true;
            })
        }
        else {
            exams.forEach(option => {
                option.disabled = false;
            }) 
        }
    }
})