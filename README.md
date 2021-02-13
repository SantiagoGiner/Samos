# Samos Academy
Samos Academy is the name I have given my tutoring classes. Samos is a small Greek island in the Aegan Sea——the birthplace of fundamental figures in science such as Pythagoras,
Aristarchus (who presented the first-known heliocentric model), and the philosopher Epicurus. I created this website as way to automate many of the processes involved with
tutoring, such as enrollment, recording of classes viewed, sharing of files, etc. I view it not only as my own platform for classes but as a way for tutees to keep track
of what they are learning, helping them have a more structured and smooth learning experience.

## Enrolling
Through this feature, new students can browse the topics I am comfortable teaching (mainly physics, math, standardized tests, chemistry, biology, and computer science). They
can then submit a form with the classes that are of interest to them. Once they enroll in a class, it will appear in their own classes section.

## Classes
This is where the classes a student is taking will appear. They can view details like the date on which they enrolled, the classes they have taken, and the zoom link for the class. Moreover, instructors can, through the Django admin page, upload files that are relevant for a certain class. These files will then appear on the student's view of the class.

## Profile
This section allows the student to create their own Samos profile, a way for instructors to get to know them and learn about their life experience. I believe it is also a way for
students to reflect on their own interests and what they want to do later in life.

## Gallery
This section contains relevant videos instructors have recorded from classes themselves or that introduce a general topic. They provide the student with material they can review outside of class.

## Admin
In the Django admin page is where instructors would be able to view and make changes to the database. Specifically, it provides the following functionalities:
* Viewing the students who have enrolled: since the Student has a many-to-many relationship with Course, one can see all the courses a specific student is taking, makin it easy to identify the necessary Course object to which to upload a file.
* Managing classes: Once an instructor finishes a tutoring session with a student, they can update the number of classes the student(s) have viewed on a particular course and    upload any relevant files to the database, using the course's id to determine in which specific instance of the Course should the file appear, i.e. which student(s) should view the file.
