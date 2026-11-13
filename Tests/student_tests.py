from Business.student_services import add_student, remove_student
from Domain.student import Student
from Repository.students_list import StudentsRepository
from Validations.student_validations import validate_student, validate_id


def test_students():
    """
    Functie care testeaza clasa Student
    :return: None
    """
    student = Student(1, "Paul Andrei", 216)
    assert student.id_student == 1
    assert student.name == "Paul Andrei"
    assert student.group == 216

def test_students_getters():
    """
    Functie care testeaza getters pentru id_student, name, group
    :return: None
    """
    student = Student(1, "Paul Andrei", 216)
    student.name = "Paul"
    assert student.name == "Paul"
    student.group = 2
    assert student.group == 2

def test_students_setters():
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

def test_students_repo():
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

def test_students_repo_add_student():
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

def test_students_repo_remove_student():
    """
    Functie care testeaza repo_remove_student
    :return: None
    """
    test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                    Student(2, "Marius", 214),
                                    Student(3, "David", 214)])
    test_repo.repo_remove_student(3)
    assert len(test_repo.students) == 2

def test_add_student():
    """
    Functie care testeaza add_student
    :return: None
    """
    test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                    Student(2, "Marius", 214),
                                    Student(3, "David", 214)])
    add_student(test_repo, 4, "Ion", 221)
    assert len(test_repo.students) == 4

def test_remove_student():
    """
    Functie care testeaza remove_student
    :return: None
    """
    test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                    Student(2, "Marius", 214),
                                    Student(3, "David", 214)])
    remove_student(test_repo, 2)
    assert len(test_repo.students) == 2

def test_validate_student():
    """
    Functie care testeaza validate_student
    :return: None
    """
    student = Student(-1, "Paul Andrei1", -216)
    try:
        validate_student(student)
        assert False
    except ValueError:
        assert True

def test_validate_id():
    """
    Functie care testeaza validate_id
    :return: None
    """
    test_repo = StudentsRepository([Student(1, "Paul Andrei", 216),
                                    Student(2, "Marius", 214),
                                    Student(3, "David", 214)])
    try:
        validate_id(test_repo, 4)
        assert False
    except ValueError:
        assert True

def run_all_student_tests():
    """
    Functie care ruleza toate testele
    :return:
    """
    test_students()
    test_students_getters()
    test_students_setters()
    test_students_repo()
    test_students_repo_add_student()
    test_students_repo_remove_student()
    test_students_repo_add_student()
    test_students_repo_remove_student()
    test_students_repo_add_student()
    test_validate_student()
    test_validate_id()

