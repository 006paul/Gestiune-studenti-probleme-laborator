from Business.lab_problem_services import add_lab_problem, remove_lab_problem
from Domain.lab_problem import LabProblem
from datetime import date
from Repository.lab_problem_list import LabProblemRepository
from Validations.lab_problem_validations import validate_lab_problem_num, validate_lab_problem, \
    validate_lab_problem_num_is_in_repo


def test_lab_problem():
    """
    Functie care testeaza clasa LabProblem si getters pt LabProblem
    :return: None
    """
    lab_problem = LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17))
    assert lab_problem.lab_num_problem_num == "lab1-p2"
    assert lab_problem.description == "A doua problema"
    assert lab_problem.deadline == date(2027, 11, 17)

def test_lab_problem_setters():
    """
    Functie care testeaza setters pt LabProblem
    :return: None
    """
    lab_problem = LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17))
    lab_problem.lab_num_problem_num = "lab1-p3"
    lab_problem.description = "A treia problema"
    lab_problem.deadline = date(2028, 11, 17)
    assert lab_problem.lab_num_problem_num == "lab1-p3"
    assert lab_problem.description == "A treia problema"
    assert lab_problem.deadline == date(2028, 11, 17)

def test_lab_repo():
    """
    Functie care testeaza clasa LabProblemRepository si getters LabProblemRepository
    :return: None
    """
    test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                          LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                          LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
    assert len(test_lab_repo_list.lab_problems) == 3
    assert test_lab_repo_list.lab_problems[1].description == "Prima problema"

def test_repo_add_lab_problem():
    """
    Functie care testeaza repo_add_lab_problem
    :return: None
    """
    test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                          LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                          LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
    lab_problem = LabProblem("lab3-p1", "l3p1", date(2027, 11, 17))
    test_lab_repo_list.repo_add_lab_problem(lab_problem)
    assert test_lab_repo_list.lab_problems[3].description == "l3p1"

def test_repo_remove_lab_problem():
    """
    Functie care testeaza repo_remove_lab_problem
    :return: None
    """
    test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                               LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                               LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
    test_lab_repo_list.repo_remove_lab_problem("lab2-p3")
    assert len(test_lab_repo_list.lab_problems) == 2

def test_add_lab_problem():
    """
    Functie care testeaza add_problem
    :return: None
    """
    test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                               LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                               LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
    test_lab_p = LabProblem("lab3-p1", "l3p1", date(2027, 11, 17))
    add_lab_problem(test_lab_repo_list, test_lab_p.lab_num_problem_num, test_lab_p.description, test_lab_p.deadline)
    assert len(test_lab_repo_list.lab_problems) == 4

def test_remove_lab_problem():
    """
    Functie care testeaza remove_lab_problem
    :return: None
    """
    test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                               LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                               LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
    remove_lab_problem(test_lab_repo_list, "lab2-p3")
    assert len(test_lab_repo_list.lab_problems) == 2

def test_validate_lab_problem_num():
    """
    Functie care testeaza validate_lab_problem_num
    :return: None
    """
    try:
        validate_lab_problem_num("lab-p")
        assert False
    except ValueError:
        assert True

def test_validate_lab_problem():
    """
    Functie care testeaza validate_lab_problem
    :return: None
    """
    lab_p = LabProblem("lab-p1", "l3p1", date(2027, 11, 17))
    try:
        validate_lab_problem(lab_p)
        assert False
    except ValueError:
        assert True

def test_validate_lab_problem_num_is_in_repo():
    """
    Functie care testeaza validate_lab_problem_num_is_in_repo
    :return: None
    """
    test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                               LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                               LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
    try:
        validate_lab_problem_num_is_in_repo(test_lab_repo_list, "lab2-p4")
        assert False
    except ValueError:
        assert True
def run_all_lab_problem_tests():
    """
    Functie care ruleaza toate testele pt problemele de laborator
    :return: None
    """
    test_lab_problem()
    test_lab_problem_setters()
    test_lab_repo()
    test_repo_add_lab_problem()
    test_repo_remove_lab_problem()
    test_add_lab_problem()
    test_remove_lab_problem()
    test_validate_lab_problem_num()
    test_validate_lab_problem()
    test_validate_lab_problem_num_is_in_repo()