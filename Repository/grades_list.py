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
        """
        Functie pentru notarea studentului la o problema asignata
        :param student: student
        :param lab_problem: problema de laborator
        :param grade: nota
        :return: None
        """
        for g in self.__grades_list:
            if g.student_id == student.id_student and g.lab_problem_num == lab_problem.lab_num_problem_num:
                if g.grade is None:
                    g.grade = grade
                    return
                else:
                    raise ValueError("Studentul este notat deja la aceasta problema")
        raise ValueError("Studentul nu are aceasta problema asignata")
    def repo_remove_student_grades(self, student_id):
        """
        Functie care sterge notele unui student care a fost sters din lista de studneti
        :param student_id: id-ul studentului
        :return: None
        """
        self.__grades_list = [g for g in self.__grades_list if g.student_id != student_id]

    def repo_remove_lab_problem_grades(self, lab_problem_num):
        """
        Functie care sterge notele de la o problema stearsa
        :param lab_problem_num: problema de laborator
        :return: None
        """
        self.__grades_list = [g for g in self.__grades_list if g.lab_problem_num != lab_problem_num]

    def repo_rename_problem_grades(self, old_num, new_num):
        """
        Functie care modifica numarul problemei de laborator din lista de note in cazul in care a fost schimbat
        :param old_num: numele vechi
        :param new_num: numele nou
        :return:
        """
        for g in self.__grades_list:
            if g.lab_problem_num == old_num:
                g.lab_problem_num = new_num

    def repo_search_grade(self, id):
        """
        Functie care cauto o nota dupa id
        :return: nota
        """
        for g in self.__grades_list:
            if g.student_id == id:
                return g
        return None
    @property
    def grades(self):
        """
        Getter pentru lista de note
        :return:
        """
        return self.__grades_list
