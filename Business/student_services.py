from Domain.student import Student
from Validations.student_validations import StudentValidations

class StudentsService:
    def add_student(self, repo, student_id, name, group):
        """
        Functie care apleaza functia repo_add_student pentru a aduga studentul student in repo
        :param repo: lista de studenti
        :param student_id: ID-ul studentului
        :param name: numele studentului
        :param group: grupa in care se afla studentul
        :return: None
        """
        student = Student(student_id, name, group)
        StudentValidations().validate_student(student)
        repo.repo_add_student(student)

    def remove_student(self, repo, student_id):
        """
        Functie care apeleaza functia repo_remove_student pentru a sterge studentul cu ID-ul id din repo
        :param repo: lista de studenti
        :param student_id: ID-ul unui student
        :return: None
        """
        repo.repo_remove_student(student_id)

    def modify_student(self, repo, student_id, name, group):
        """
        Functie care apeleaza metoda repo_modify_students
        :param repo: lista de studenti
        :param student_id: ID-ul unui student
        :param name: numele unui student
        :param group: grupa unui student
        :return: None
        """
        student = Student(student_id, name, group)
        StudentValidations().validate_student(student)
        repo.repo_modify_students(student)

    def search_students(self, repo, student_id : int):
        """
        Functie care apeleaza metoda repo_search_students
        :param repo: lista de studenti
        :param student_id: id-ul studentului cautat
        :return: student
        """
        student = repo.repo_search_students(student_id)
        return student
