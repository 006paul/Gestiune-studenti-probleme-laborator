from Business.grade_service import GradesService
from Business.lab_problem_services import LabProblemService
from Business.student_services import StudentsService
from datetime import datetime
from Repository.students_list import StudentsRepository


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

    def ui_print_grades_list(self, repo, lab_repo, grade_repo):
        """
        Functie care afiseaza toate problemele de laborator asignate
        :param repo: lista de studenti
        :param lab_repo: lista de probleme de laborator
        :param grade_repo: lista de note
        :return: None
        """
        for grade in grade_repo.grades:
            print(grade)

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

    def ui_remove_student(self, repo, grade_repo):
        """
        Functie care initiaza stergerea unui student din lista de studenti
        :param repo: lista de studenti
        :return: None
        """
        try:
            id_to_remove = int((input("Dati ID-ul studentului pe care doriti sa-l stergeti: ")).strip())
            StudentsService().remove_student(repo, grade_repo, id_to_remove)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_remove_lab_problem(self, lab_repo, grades_repo):
        """
        Funcite care initiaza stergerea unei probleme din lista de probleme de laborator lab_repo
        :param lab_repo: lista de probleme de laborator
        :return: None
        """
        try:
            p_to_remove = input("Dati numarul laboratorului si numarul problemei pe care doriti sa-l stergeti (labX-pY): ").lower().strip()
            LabProblemService().remove_lab_problem(lab_repo, grades_repo, p_to_remove)
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

    def ui_modify_lab_problem(self, lab_repo, grades_repo):
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
                LabProblemService().modify_lab_problem(lab_repo, grades_repo, p_to_modify, lab_num_lab_problem, description, deadline_date)
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

    def ui_assign_problem(self, repo, lab_repo, grades_repo):
        """
        Functie care initializeaza asignarea unei probleme unui student
        :param repo: lista de studenti
        :param lab_repo: lista de probleme de laborator
        :param grades_repo: lista de note
        :return: None
        """
        try:
            student_id = int(input("Dati ID-ul studentului caruia doriti sa-i asignati o problema: ").strip())
            lab_p = input("Dati numarul problemei pe care doriti sa i-o asignati studentului (labX-pY): ").lower().strip()
            GradesService().assign_problem(repo, lab_repo, grades_repo, student_id, lab_p)
        except ValueError as e:
            print(f"Eroare: \n{e}")

    def ui_grade_assigned_problem(self, repo, lab_repo, grades_repo):
        """
        Functie care initializeaza asignarea unei probleme unui student
        :param repo: lista de studenti
        :param lab_repo: lista de probleme de laborator
        :param grades_repo: lista de note
        :return: None
        """
        try:
            student_id = int(input("Dati ID-ul studentului pe care doriti sa-l notati: ").strip())
            lab_p = input("Dati numarul problemei (labX-pY): ").lower().strip()
            problem_grade = float(input("Dati nota: ").strip())
            GradesService().grade_assigned_problem(repo, lab_repo, grades_repo, student_id, lab_p, problem_grade)
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
              "11: Afiseaza toti studentii cu probleme asignate \n"
              "12: Asigneaza o problema de laborator unui student \n"
              "13: Noteza un student \n"
              "exit: Opreste programul \n"
              "-----------------------------------------------------")

    def ui_run_console(self, command, repo, lab_repo, grades_repo):
        """
        Functie care ruleaza comenzile de la utilizator
        :param command: str - comanda data de utilizator
        :param repo: lista de studenti
        :param lab_repo: lista de probleme de laborator
        :return: none
        """
        student_commands = {
            "1": lambda: self.ui_print_all_students(repo),
            "3": lambda: self.ui_add_student(repo),
            "4": lambda: self.ui_remove_student(repo, grades_repo),
            "5": lambda: self.ui_modify_student_by_id(repo),
            "6": lambda: self.ui_search_students(repo),
                    }
        problem_commands = {
            "2": lambda: self.ui_print_all_lab_problems(lab_repo),
            "7": lambda: self.ui_add_lab_problem(lab_repo),
            "8": lambda: self.ui_remove_lab_problem(lab_repo, grades_repo),
            "9": lambda: self.ui_modify_lab_problem(lab_repo, grades_repo),
            "10": lambda: self.ui_search_lab_problem(lab_repo),
        }
        assignment_commands = {
            "11" : lambda:  self.ui_print_grades_list(repo, lab_repo, grades_repo),
            "12" : lambda: self.ui_assign_problem(repo, lab_repo, grades_repo),
            "13" : lambda: self.ui_grade_assigned_problem(repo, lab_repo, grades_repo),
        }
        if command in student_commands:
            student_commands[command]()
        elif command in problem_commands:
            problem_commands[command]()
        elif command in assignment_commands:
            assignment_commands[command]()
        else:
            print("Comanda invalida")

    def ui_get_command(self):
        """
        Functie care citeste de la tastatura comanda command
        :return: command - str, comanda data de utilizator
        """
        command = (input()).strip()
        return command