from datetime import date

def validate_lab_problem_num(lab_problem_num):
    """
    Functie care valideaza corectitudinea formatului pentru lab_num_problem_num
    :param lab_problem: problema de laborator
    :return: None
    """
    errors = []
    parts = lab_problem_num.split("-")
    if not len(parts) == 2 or not parts[0].startswith("lab") or not parts[1].startswith("p"):
        raise ValueError("Format gresit pentru labX-pY")
    lab_str = parts[0][3:]
    p_str = parts[1][1:]

    if not lab_str.isdigit() or not int(lab_str) > 0:
        errors.append("Numarul laboratorului trebuie sa fie numar natural")
    if not p_str.isdigit() or not int(p_str) > 0:
        errors.append("Numarul problemei trebuie sa fie numar natural")
    if len(errors) > 0:
        raise ValueError("\n".join(errors))
def validate_lab_problem(lab_problem):
    """
    Functie care valideaza problema de laborator lab_problem
    :param lab_problem: problema de laborator
    :return: None
    """
    errors = []
    validate_lab_problem_num(lab_problem.lab_num_problem_num)
    if not lab_problem.description.strip():
        errors.append("Descrierea nu poate fi vida")

    if lab_problem.deadline < date.today():
        errors.append("Deadline-ul nu poate fi in trecut")

    if len(errors) > 0:
        raise ValueError("\n".join(errors))

def validate_lab_problem_num_is_in_repo(lab_repo, lab_problem_num):
    """
    Functie care valideaza daca numarul problemei lab_problem_num se alfa in lab_repo
    :param lab_repo: lista de probleme de laborator
    :param lab_problem_num: lista de probleme de laborator
    :return: None
    """
    validate_lab_problem_num(lab_problem_num)
    ok = False
    for problem in lab_repo.lab_problems:
        if problem.lab_num_problem_num == lab_problem_num:
            ok = True
    if not ok:
        raise ValueError("Problema nu exista")

