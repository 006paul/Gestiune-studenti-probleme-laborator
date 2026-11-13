from Business.lab_problem_services import add_lab_problem, remove_lab_problem, modify_lab_problem
from Business.student_services import add_student, remove_student, modify_student
from datetime import datetime

def ui_print_all_students(repo):
    """
    Functie care afiseaza toti studentii
    :param repo: Lista de studenti
    :return: None
    """
    for student in repo.students:
        print(student)

def ui_print_all_lab_problems(lab_repo):
    """
    Functie care afiseaza toate problemele de laborator
    :param lab_repo: lista de probleme de laborator
    :return: None
    """
    for problem in lab_repo.lab_problems:
        print(problem)

def ui_add_student(repo):
    """
    Functie care initializeaza adaugarea unui student in lista de studenti
    :param repo: lista de studenti
    :return: None
    """
    try:
        id_student = int((input("Dati ID-ul studentului: ")).strip())
        name_student = (input("Dati numele studentului: ")).strip()
        group_student = int((input("Dati grupa studentului: ")).strip())
        add_student(repo, id_student, name_student, group_student)
    except ValueError as e:
        print(f"Eroare: \n{e}")

def ui_add_lab_problem(lab_repo):
    """
    Functie care initializeaza adaugarea unei porbleme de laborator
    :param lab_repo: lista de probleme de laborator
    :return: None
    """
    try:
        lab_num_lab_problem = input("Dati numarul laboratorului si al problemei (labX-pY): ").lower().strip()
        description = input("Dati descierea problemei: ").strip()
        deadline = input("Dati deadline-ul (zz/ll/aaaa): ").strip()
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y").date()
        add_lab_problem(lab_repo, lab_num_lab_problem, description, deadline_date)
    except ValueError as e:
        print(f"Eroare: \n{e}")

def ui_remove_student(repo):
    """
    Functie care initiaza stergerea unui student din lista de studenti
    :param repo: lista de studenti
    :return: None
    """
    try:
        id_to_remove = int((input("Dati ID-ul studentului pe care doriti sa-l stergeti: ")).strip())
        remove_student(repo, id_to_remove)
    except ValueError as e:
        print(f"Eroare: \n{e}")

def ui_remove_lab_problem(lab_repo):
    """
    Funcite care initiaza stergerea unei probleme din lista de probleme de laborator lab_repo
    :param lab_repo: lista de probleme de laborator
    :return: None
    """
    try:
        p_to_remove = input("Dati numarul laboratorului si numarul problemei pe care doriti sa-l stergeti (labX-pY): ").lower().strip()
        remove_lab_problem(lab_repo, p_to_remove)
    except ValueError as e:
        print(f"Eroare: \n{e}")

def ui_modify_student_by_id(repo):
    """
    Functie care initializeaza modificarea unui student din lista de studenti
    :param repo: lista de studenti
    :return: None
    """
    try:
        s_to_modify = int(input("Dati ID-ul studentului pe care vreti sa-l modificati: ").strip())
        try:
            name_student = (input("Dati numele studentului: ")).strip()
            group_student = int((input("Dati grupa studentului: ")).strip())
            modify_student(repo, s_to_modify, name_student, group_student)
        except ValueError as e:
            print(f"Eroare: \n{e}")
    except ValueError as e:
        print(f"Eroare: \n{e}")

def ui_modify_lab_problem(lab_repo):
    """
    Fucntie care initializeaza modificarea unei probleme din lista de probleme de laborator lab_repo
    :param lab_repo: lista de probleme de laborator
    :return: None
    """
    try:
        p_to_modify = input("Dati numarul laboratorului si problemei pe care vreti sa o modificati (labX-pY): ").lower().strip()
        try:
            lab_num_lab_problem = input("Dati numarul laboratorului si al problemei (labX-pY): ").lower().strip()
            description = input("Dati descierea problemei: ").strip()
            deadline = input("Dati deadline-ul (zz/ll/aaaa): ").strip()
            deadline_date = datetime.strptime(deadline, "%d/%m/%Y").date()
            modify_lab_problem(lab_repo, p_to_modify, lab_num_lab_problem, description, deadline_date)
        except ValueError as e:
            print(f"Eroare: \n{e}")
    except ValueError as e:
        print(f"Eroare: \n{e}")
def ui_menu():
    """
    Functie care afiseaza meniul aplicatiei
    :return: None
    """
    print("----------------------------------------------------- \n"
          "1: Afiseaza toti studentii \n"
          "2: Afiseaza toate problemele de laborator \n"
          "3: Adauga un student \n"
          "4: Sterge un student \n"
          "5: Modifica un student (dupa ID): \n"
          "6: Adauga o problema de laborator \n"
          "7: Sterge o problema de laborator \n"
          "8: Modifica o problema de laborator \n"
          "exit: Opreste programul \n"
          "-----------------------------------------------------")

def ui_run_console(command, repo, lab_repo):
    """
    Functie care ruleaza comenzile de la utilizator
    :param command: str - comanda data de utilizator
    :param repo: lista de studenti
    :param lab_repo: lista de probleme de laborator
    :return: none
    """
    student_commands = {
        "1": ui_print_all_students,
        "3": ui_add_student,
        "4": ui_remove_student,
        "5": ui_modify_student_by_id,
                }
    problem_commands = {
        "2": ui_print_all_lab_problems,
        "6": ui_add_lab_problem,
        "7": ui_remove_lab_problem,
        "8": ui_modify_lab_problem,
    }
    if command in student_commands:
        student_commands[command](repo)
    elif command in problem_commands:
        problem_commands[command](lab_repo)
    else:
        print("Comanda invalida")

def ui_get_command():
    """
    Functie care citeste de la tastatura comanda command
    :return: command - str, comanda data de utilizator
    """
    command = (input()).strip()
    return command