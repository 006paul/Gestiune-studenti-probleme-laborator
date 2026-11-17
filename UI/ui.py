from Business.lab_problem_services import LabProblemService
from Business.student_services import StudentsService
from datetime import datetime

class UI:
    def ui_print_all_students(self, repo):
        """
        Functie care afiseaza toti studentii
        :param repo: Lista de studenti
        :return: None
        """
        for student in repo.students:
            print(student)

    def ui_print_all_lab_problems(self, lab_repo):
        """
        Functie care afiseaza toate problemele de laborator
        :param lab_repo: lista de probleme de laborator
        :return: None
        """
        for problem in lab_repo.lab_problems:
            print(problem)

    def ui_add_student(self, repo):
        """
        Functie care initializeaza adaugarea unui student in lista de studenti
        :param repo: lista de studenti
        :return: None
        """
        try:
            id_student = int((input("Dati ID-ul studentului: ")).strip())
            name_student = (input("Dati numele studentului: ")).strip()
            group_student = int((input("Dati grupa studentului: ")).strip())
            StudentsService().add_student(repo, id_student, name_student, group_student)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_add_lab_problem(self, lab_repo):
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
            LabProblemService().add_lab_problem(lab_repo, lab_num_lab_problem, description, deadline_date)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_remove_student(self, repo):
        """
        Functie care initiaza stergerea unui student din lista de studenti
        :param repo: lista de studenti
        :return: None
        """
        try:
            id_to_remove = int((input("Dati ID-ul studentului pe care doriti sa-l stergeti: ")).strip())
            StudentsService().remove_student(repo, id_to_remove)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_remove_lab_problem(self, lab_repo):
        """
        Funcite care initiaza stergerea unei probleme din lista de probleme de laborator lab_repo
        :param lab_repo: lista de probleme de laborator
        :return: None
        """
        try:
            p_to_remove = input("Dati numarul laboratorului si numarul problemei pe care doriti sa-l stergeti (labX-pY): ").lower().strip()
            LabProblemService().remove_lab_problem(lab_repo, p_to_remove)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_modify_student_by_id(self, repo):
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
                StudentsService().modify_student(repo, s_to_modify, name_student, group_student)
            except ValueError as e:
                print(f"Eroare: \n{e}")
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_modify_lab_problem(self, lab_repo):
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
                LabProblemService().modify_lab_problem(lab_repo, p_to_modify, lab_num_lab_problem, description, deadline_date)
            except ValueError as e:
                print(f"Eroare: \n{e}")
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_search_students(self, repo):
        """
        Functie care initializeaza cautarea unui student
        :param repo: lista de studenti
        :return: None
        """
        try:
            student_id = int(input("Dati ID-ul studentului pe care doriti sa-l cautati: ").strip())
            student = StudentsService().search_students(repo, student_id)
            print(student)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_search_lab_problem(self, lab_repo):
        """
        Functie care initializeaza cautarea unei probleme de laborator
        :param lab_repo: lista de probleme de laborator
        :return: None
        """
        try:
            lab_num_problem_num = input("Dati numarul problemei de laborator pe care doriti sa o cautati (labX-pY): ").lower().strip()
            lab_p = LabProblemService().search_lab_problem(lab_repo, lab_num_problem_num)
            print(lab_p)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_menu(self):
        """
        Functie care afiseaza meniul aplicatiei
        :return: None
        """
        print("----------------------------------------------------- \n"
              "1: Afiseaza toti studentii \n"
              "2: Afiseaza toate problemele de laborator \n"
              "3: Adauga un student \n"
              "4: Sterge un student \n"
              "5: Modifica un student (dupa ID) \n"
              "6: Cauta un student (dupa ID) \n"
              "7: Adauga o problema de laborator \n"
              "8: Sterge o problema de laborator \n"
              "9: Modifica o problema de laborator \n"
              "10: Cauta o problema de laborator \n"
              "exit: Opreste programul \n"
              "-----------------------------------------------------")

    def ui_run_console(self, command, repo, lab_repo):
        """
        Functie care ruleaza comenzile de la utilizator
        :param command: str - comanda data de utilizator
        :param repo: lista de studenti
        :param lab_repo: lista de probleme de laborator
        :return: none
        """
        student_commands = {
            "1": self.ui_print_all_students,
            "3": self.ui_add_student,
            "4": self.ui_remove_student,
            "5": self.ui_modify_student_by_id,
            "6": self.ui_search_students,
                    }
        problem_commands = {
            "2": self.ui_print_all_lab_problems,
            "7": self.ui_add_lab_problem,
            "8": self.ui_remove_lab_problem,
            "9": self.ui_modify_lab_problem,
            "10": self.ui_search_lab_problem,
        }
        if command in student_commands:
            student_commands[command](repo)
        elif command in problem_commands:
            problem_commands[command](lab_repo)
        else:
            print("Comanda invalida")

    def ui_get_command(self):
        """
        Functie care citeste de la tastatura comanda command
        :return: command - str, comanda data de utilizator
        """
        command = (input()).strip()
        return command