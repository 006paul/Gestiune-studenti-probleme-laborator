from Domain.lab_problem import LabProblem
from Validations.lab_problem_validations import validate_lab_problem, validate_lab_problem_num, \
    validate_lab_problem_num_is_in_repo


def add_lab_problem(lab_repo, lab_num_lab_problem, description, deadline):
    """
    Functie care apeleaza metoda repo_add_lab_problem
    :param lab_repo: lista de probleme de laborator
    :param lab_num_lab_problem: numarul laboratorului si numarul problemei
    :param description: descrierea problemei
    :param deadline: deadline-ul problemei
    :return: None
    """
    lab_problem = LabProblem(lab_num_lab_problem, description, deadline)
    validate_lab_problem(lab_problem)
    lab_repo.repo_add_lab_problem(lab_problem)

def remove_lab_problem(lab_repo, lab_problem_num):
    """
    Functie care apeleza metoda repo_remove_lab_problem
    :param lab_repo: lista de probleme de laborator
    :param lab_num_lab_problem: numarul problemei care va fi stearsa
    :return: None
    """
    validate_lab_problem_num_is_in_repo(lab_repo, lab_problem_num)
    lab_repo.repo_remove_lab_problem(lab_problem_num)