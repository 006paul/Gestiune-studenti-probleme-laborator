from Domain.student import Student
from Repository.lab_problem_list import LabProblemRepository
from Repository.students_list import StudentsRepository
from Validations.grade_validations import GradeValidations


class GradesService:
    def assign_problem(self, repo, lab_repo, grades_repo, student_id, lab_problem):
        """
        Functie care apeleaza metoda repo_assign_problem
        :param grades_repo: lista de note
        :param student_id: id-ul studentului caruia i se asigneaza problema lab-problem
        :param lab_problem: problema care se asigneaza
        :return: None
        """
        student = StudentsRepository.repo_search_students(repo, student_id)
        lab_p = LabProblemRepository.repo_search_lab_problem(lab_repo, lab_problem)
        grades_repo.repo_assign_problem(student, lab_p)

    def grade_assigned_problem(self, repo, lab_repo, grades_repo, student_id, lab_problem, grade):
        """
        Functie care apela metoda repo_grade_assigned_problem
        :param repo: lista de studenti
        :param lab_repo: lista de probleme de laborator
        :param grades_repo: lista de note
        :param student_id: id-ul studentului notat
        :param lab_problem: nr problemei notate
        :param grade: nota
        :return: None
        """
        student = StudentsRepository.repo_search_students(repo, student_id)
        lab_p = LabProblemRepository.repo_search_lab_problem(lab_repo, lab_problem)
        GradeValidations().validate_grade(grade)
        grades_repo.repo_grade_assigned_problem(student, lab_p, grade)