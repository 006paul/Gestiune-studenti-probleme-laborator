from datetime import date

from Business.grade_service import GradesService
from Domain.grade import Grade
from Domain.lab_problem import LabProblem
from Domain.student import Student
from Repository.grades_list import GradeRepository
from Repository.lab_problem_list import LabProblemRepository
from Repository.students_list import StudentsRepository
from Validations.grade_validations import GradeValidations


class GradesTests:
    def test_grade(self):
        """
        Functie care testeaza constructorul clasei grade si getters
        :return: None
        """
        grade = Grade(1, "lab1-p1", 7)
        assert grade.student_id == 1
        assert grade.lab_problem_num == "lab1-p1"
        assert grade.grade == 7

    def test_grade_setters(self):
        """
        Functie care testeaza grade setters
        :return: None
        """
        grade = Grade(1, "lab1-p1", 7)
        try:
            grade.grade = "abc"
            assert False
        except ValueError:
            assert True
        grade.lab_problem_num = "lab1-p2"
        grade.grade = 9
        assert grade.lab_problem_num == "lab1-p2"
        assert grade.grade == 9

    def test_grades_repo(self):
        """
        Functie care testeaza GradeRepository
        :return: None
        """
        test_grades_repo = GradeRepository([Grade(1, "lab1-p1", 7),
                                            Grade(2, "lab1-p2", 8),
                                            Grade(3, "lab1-p3", 5)])
        assert len(test_grades_repo.grades) == 3

    def test_grade_validation(self):
        """
        Functie care testeaza functia grade_validation
        :return: None
        """
        grade = Grade(1, "lab1-p1", 7.0)
        try:
            GradeValidations().validate_grade(11)
            assert False
        except ValueError:
            assert True

    def test_repo_assgin_lab_problem(self):
        """
        Functie care testeaza repo_assgin_lab_problem
        :return: None
        """
        student = Student(1, "paul", 216)
        lab_p = LabProblem("lab1-p2", "descriere", date(2028, 11, 17))
        test_grade_repo = GradeRepository([])
        test_grade_repo.repo_assign_problem(student, lab_p)
        assert len(test_grade_repo.grades) == 1
        try:
            test_grade_repo.repo_assign_problem(student, lab_p)
            assert False
        except ValueError:
            assert True

    def test_repo_grade_assigned_problem(self):
        """
        Functie care testeaza repo_grade_assigned_problem
        :return: None
        """
        student = Student(1, "paul", 216)
        lab_p1 = LabProblem("lab1-p1", "descriere", date(2028, 11, 17))
        lab_p2 = LabProblem("lab1-p2", "descriere", date(2028, 11, 17))
        test_grade_repo = GradeRepository([Grade(1, "lab1-p1", 7)])
        try:
            test_grade_repo.repo_grade_assigned_problem(student, lab_p1, 8)
            assert False
        except ValueError:
            assert True
        try:
            test_grade_repo.repo_grade_assigned_problem(student, lab_p2, 9)
            assert False
        except ValueError:
            assert True

    def test_repo_remove_student_grades(self):
        """
        Functie care testeaza repo_remove_student_grades
        :return: None
        """
        test_grade_repo = GradeRepository([Grade(1, "lab1-p1", 7),
                                           Grade(2, "lab1-p2", 8),
                                           Grade(3, "lab1-p3", 5)])
        test_grade_repo.repo_remove_student_grades(1)
        assert len(test_grade_repo.grades) == 2

    def test_repo_remove_lab_problem_grades(self):
        """
        Functie care testeaza remove_lab_problem_grades
        :return: None
        """
        test_grade_repo = GradeRepository([Grade(1, "lab1-p1", 7),
                                           Grade(2, "lab1-p2", 8),
                                           Grade(3, "lab1-p3", 5)])
        test_grade_repo.repo_remove_lab_problem_grades("lab1-p1")
        assert len(test_grade_repo.grades) == 2

    def test_repo_rename_problem_grades(self):
        """
        Functie care testeaza repo_rename_problem_grades
        :return: None
        """
        test_grade_repo = GradeRepository([Grade(1, "lab1-p1", 7),
                                           Grade(2, "lab1-p2", 8),
                                           Grade(3, "lab1-p3", 5)])
        test_grade_repo.repo_rename_problem_grades("lab1-p1", "lab1-p5")
        assert test_grade_repo.grades[0].lab_problem_num == "lab1-p5"

    def test_assign_lab_problem(self):
        """
        Functie care testeaza assign_lab_problem
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "paul", 216)])
        test_lab_repo = LabProblemRepository([LabProblem("lab1-p1", "lab1-p1", date(2028, 11, 17))])
        test_grade_repo = GradeRepository([])
        GradesService().assign_problem(test_repo, test_lab_repo, test_grade_repo, 1, "lab1-p1")
        assert len(test_grade_repo.grades) == 1

    def test_grade_assigned_problem(self):
        """
        Functie care testeaza grade_assigned_problem
        :return: None
        """
        test_repo = StudentsRepository([Student(1, "paul", 216)])
        test_lab_repo = LabProblemRepository([LabProblem("lab1-p1", "lab1-p1", date(2028, 11, 17))])
        test_grade_repo = GradeRepository([])
        GradesService().assign_problem(test_repo, test_lab_repo, test_grade_repo, 1, "lab1-p1")
        GradesService().grade_assigned_problem(test_repo, test_lab_repo, test_grade_repo, 1, "lab1-p1", 10)
        assert test_grade_repo.grades[0].grade == 10

    def test_repo_search_grade(self):
        """
        Functie care testeaza repo_search_grade
        :return: None
        """

        def test_repo_search_grade(self):
            grades_repo = GradeRepository([
                Grade(1, "lab1-p1", 7),
                Grade(1, "lab2-p1", 9),
            ])

            found_grade = grades_repo.repo_search_grade(1, "lab2-p1")
            assert found_grade == grades_repo.grades[1]

            missing_grade = grades_repo.repo_search_grade(1, "lab3-p1")
            assert missing_grade is None

    def run_all_grade_tests(self):
        """
        Functie care ruleaza toate testele
        :return: None
        """
        self.test_grade()
        self.test_grade_setters()
        self.test_grades_repo()
        self.test_grade_validation()
        self.test_repo_assgin_lab_problem()
        self.test_repo_grade_assigned_problem()
        self.test_repo_remove_student_grades()
        self.test_repo_remove_lab_problem_grades()
        self.test_repo_rename_problem_grades()
        self.test_assign_lab_problem()
        self.test_grade_assigned_problem()
        self.test_repo_search_grade()