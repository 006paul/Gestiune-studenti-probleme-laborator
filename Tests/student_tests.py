from Business.student_services import StudentsService
from Domain.grade import Grade
from Domain.student import Student
from Repository.grades_list import GradeRepository
from Repository.students_list import StudentsRepository
from Validations.student_validations import StudentValidations


class StudentsTests:
    def test_students(self):
        """
        Functie care testeaza clasa Student
        :return: None
        """
        student = Student(1, "Paul Andrei", 216)
        assert student.id_student == 1
        assert student.name == "Paul Andrei"
        assert student.group == 216

    def test_students_getters(self):
        """
        Functie care testeaza getters pentru id_student, name, group
        :return: None
        """
        student = Student(1, "Paul Andrei", 216)
        student.name = "Paul"
        assert student.name == "Paul"
        student.group = 2
        assert student.group == 2

    def test_students_setters(self):
        """
        Functie care testeaza setters pentru name, group
        :return: None
        """
        student = Student(1, "Paul Andrei", 216)
        try:
            student.name = ""
            assert False
        except ValueError:
            assert True
        try:
            student.group = -1
            assert False
        except ValueError:
            assert True

    def test_students_repo(self):
        """
        Functie care testeaza clasa StudentsRepository
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        assert len(test_repo.students) == 3
        assert test_repo.students[0].id_student == 1
        assert test_repo.students[0].name == "Paul Andrei"
        assert test_repo.students[0].group == 216

    def test_students_repo_add_student(self):
        """
        Functie care testeaza repo_add_student
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        student = Student(4, "Ion", 211)
        test_repo.repo_add_student(student)
        assert len(test_repo.students) == 4

    def test_students_repo_remove_student(self):
        """
        Functie care testeaza repo_remove_student
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        test_repo.repo_remove_student(3)
        assert len(test_repo.students) == 2

    def test_add_student(self):
        """
        Functie care testeaza add_student
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        StudentsService().add_student(test_repo, 4, "Ion", 221)
        assert len(test_repo.students) == 4

    def test_remove_student(self):
        """
        Functie care testeaza remove_student
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        test_grades_repo = GradeRepository([
            Grade(1, "lab1-p1", 9.5),
            Grade(2, "lab1-p1", 8.0)])
        StudentsService().remove_student(test_repo, test_grades_repo, 2)
        assert len(test_repo.students) == 2

    def test_validate_student(self):
        """
        Functie care testeaza validate_student
        :return: None
        """
        student = Student(-1, "Paul Andrei1", -216)
        try:
            StudentValidations().validate_student(student)
            assert False
        except ValueError:
            assert True

    def test_modify_student(self):
        """
        Functie care testeaza modify_student
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        StudentsService().modify_student(test_repo, 3, "Ion", 221)
        assert test_repo.students[2].group == 221

    def test_repo_modify_student(self):
        """
        Functie care testeaza repo_modify_student
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                        Student(2, "Marius", 214),
                                        Student(3, "David", 214)])
        student = Student(3, "Ion", 221)
        test_repo.repo_modify_students(student)
        assert test_repo.students[2].group == 221

    def test_repo_search_students(self):
        """
        Functie care testeaza repo_search_students
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),])
        searched_student = test_repo.repo_search_students(1)
        assert test_repo.students[0] == searched_student

    def test_search_students(selfs):
        """
        Functie care testeaza search_students
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "Paul Andrei", 216), ])
        searched_student = StudentsService().search_students(test_repo, 1)
        assert test_repo.students[0] == searched_student

    def run_all_student_tests(self):
        """
        Functie care ruleza toate testele
        :return:
        """
        self.test_students()
        self.test_students_getters()
        self.test_students_setters()
        self.test_students_repo()
        self.test_students_repo_add_student()
        self.test_students_repo_remove_student()
        self.test_add_student()
        self.test_remove_student()
        self.test_validate_student()
        self.test_modify_student()
        self.test_repo_modify_student()
        self.test_repo_search_students()
        self.test_search_students()