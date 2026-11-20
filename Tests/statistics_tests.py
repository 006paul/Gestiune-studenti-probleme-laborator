from Business.statistics_service import StatisticsService
from Domain.grade import Grade
from Domain.student import Student
from Repository.grades_list import GradeRepository
from Repository.students_list import StudentsRepository


class StatisticsTests:
    def test_sort_students_and_grades_by_name(self):
        """
        Functie care testeaza sort_students_and_grades_by_name
        :return: None
        """
        students = [
            Student(3, "paul", 216),
            Student(2, "Andrei", 216),
            Student(1, "andrei", 216),
        ]
        repo = StudentsRepository(students.copy())

        result = StatisticsService().sort_students_and_grades_by_name(repo)

        assert [student.id_student for student in result] == [1, 2, 3]
        assert [student.id_student for student in repo.students] == [3, 2, 1]

    def test_sort_students_by_grade(self):
        """
        Functie care testeaza sort_students_by_grade
        :return: None
        """
        repo = StudentsRepository([
            Student(1, "Paul", 216),
            Student(2, "Andrei", 216),
            Student(3, "Mihai", 216),
            Student(4, "Ana", 216),
            Student(5, "Ioana", 216),
        ])
        grades_repo = GradeRepository([
            Grade(1, "lab2-p1", 10),
            Grade(1, "lab1-p1", 4.0),
            Grade(2, "lab1-p1", 4.01),
            Grade(3, "lab1-p1", 3.0),
            Grade(4, "lab1-p1", None),
            Grade(5, "lab2-p1", 9.0),
        ])

        result = StatisticsService().sort_students_by_grade(
            repo, grades_repo, "lab1-p1"
        )

        assert [student.id_student for student, _ in result] == [2, 1, 3, 4]
        assert [grade.grade for _, grade in result] == [4.01, 4.0, 3.0, None]

    def test_sort_students_by_grade_with_no_matching_assignments(self):
        """
        Functie care testeaza sort_students_by_grade
        :return: None
        """
        repo = StudentsRepository([Student(1, "Paul", 216)])
        grades_repo = GradeRepository([Grade(1, "lab2-p1", 8.0)])

        result = StatisticsService().sort_students_by_grade(
            repo, grades_repo, "lab1-p1"
        )

        assert result == []

    def test_students_with_average_less_than_five(self):
        """
        Functie care testeaza sort_students_with_average_less_than_five
        :return:
        """
        repo = StudentsRepository([
            Student(1, "Paul", 216),
            Student(2, "Andrei", 216),
            Student(3, "Mihai", 216),
            Student(4, "Ana", 216),
        ])
        grades_repo = GradeRepository([
            Grade(1, "lab1-p1", 4.0),
            Grade(1, "lab1-p2", 5.0),
            Grade(2, "lab1-p1", 5.0),
            Grade(2, "lab1-p2", None),
            Grade(3, "lab1-p1", 2.0),
            Grade(3, "lab1-p2", None),
        ])

        result = StatisticsService().students_with_average_less_than_five(
            repo, grades_repo
        )

        assert [student.id_student for student, _ in result] == [1, 3]
        assert [average for _, average in result] == [4.5, 2.0]

    def run_all_statistics_tests(self):
        self.test_sort_students_and_grades_by_name()
        self.test_sort_students_by_grade()
        self.test_sort_students_by_grade_with_no_matching_assignments()
        self.test_students_with_average_less_than_five()
