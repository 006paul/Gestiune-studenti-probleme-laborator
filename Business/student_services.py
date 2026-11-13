from Domain.student import Student
from Validations.student_validations import validate_student, validate_id


def add_student(repo, student_id, name, group):
    """
    Functie care apleaza functia repo_add_student pentru a aduga studentul student in repo
    :param repo: lista de studenti
    :param student_id: ID-ul studentului
    :param name: numele studentului
    :param group: grupa in care se afla studentul
    :return: None
    """
    student = Student(student_id, name, group)
    validate_student(student)
    repo.repo_add_student(student)

def remove_student(repo, student_id):
    """
    Functie care apeleaza functia repo_remove_student pentru a sterge studentul cu ID-ul id din repo
    :param repo: lista de studenti
    :param student_id: ID-ul unui student
    :return: None
    """
    validate_id(repo, student_id)
    repo.repo_remove_student(student_id)
