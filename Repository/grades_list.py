from Domain.grade import Grade
from Domain.lab_problem import LabProblem
from Domain.student import Student


class GradeRepository:

    def __init__(self, grades_list):
        """
        Constructorul clasei GradeRepository
        :param grades_list:
        """
        self.__grades_list = grades_list

    def repo_assign_problem(self, student : Student, lab_problem : LabProblem):
        """
        Functie care asigneaza o problema lab_problem unui student student
        :param student: student
        :param lab_problem: problema de laborator
        :return: None
        """
        for g in self.__grades_list:
            if g.student_id == student.id_student and g.lab_problem_num == lab_problem.lab_num_problem_num:
                raise ValueError("Studentul are deja problema asignata")
        assigned_problem = Grade(student.id_student, lab_problem.lab_num_problem_num)
        self.__grades_list.append(assigned_problem)

    def repo_grade_assigned_problem(self, student : Student, lab_problem : LabProblem, grade : float | int):
        for g in self.__grades_list:
            if g.student_id == student.id_student and g.lab_problem_num == lab_problem.lab_num_problem_num:
                if g.grade is None:
                    g.grade = grade
                    return
                else:
                    raise ValueError("Studentul este notat deja la aceasta problema")
        raise ValueError("Studentul nu are aceasta problema asignata")

    @property
    def grades(self):
        """
        Getter pentru lista de note
        :return:
        """
        return self.__grades_list
