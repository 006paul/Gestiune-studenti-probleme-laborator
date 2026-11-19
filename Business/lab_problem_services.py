from Domain.lab_problem import LabProblem
from Validations.lab_problem_validations import LabProblemValidations

class LabProblemService:
    def add_lab_problem(self, lab_repo, lab_num_lab_problem, description, deadline):
        """
        Functie care apeleaza metoda repo_add_lab_problem
        :param lab_repo: lista de probleme de laborator
        :param lab_num_lab_problem: numarul laboratorului si numarul problemei
        :param description: descrierea problemei
        :param deadline: deadline-ul problemei
        :return: None
        """
        lab_problem = LabProblem(lab_num_lab_problem, description, deadline)
        LabProblemValidations().validate_lab_problem(lab_problem)
        lab_repo.repo_add_lab_problem(lab_problem)

    def remove_lab_problem(self, lab_repo, grades_repo, lab_problem_num : str):
        """
        Functie care apeleza metoda repo_remove_lab_problem
        :param lab_repo: lista de probleme de laborator
        :param lab_problem_num: numarul problemei care va fi stearsa
        :return: None
        """
        lab_repo.repo_remove_lab_problem(lab_problem_num)
        grades_repo.repo_remove_lab_problem_grades(lab_problem_num)


    def modify_lab_problem(self, lab_repo, grades_repo,
                           p_to_modify : str, lab_num_lab_problem : str, description : str, deadline):
        """
        Functie care apeleza metoda repo_modify_lab_problem
        :param lab_repo: lista de probleme de laborator
        :param p_to_modify: numarul problemei care va fi modificata
        :param lab_num_lab_problem: numarul laboratorului si al problemei
        :param description: descrierea problemei
        :param deadline: deadline-ul problemei
        :return: None
        """
        lab_problem = LabProblem(lab_num_lab_problem, description, deadline)
        LabProblemValidations().validate_lab_problem(lab_problem)
        lab_repo.repo_modify_lab_problem(p_to_modify, lab_problem)
        grades_repo.repo_rename_problem_grades(p_to_modify, lab_num_lab_problem)

    def search_lab_problem(self, lab_repo, lab_num_problem_num):
        """
        Funcite care apeleaza metoda repo_search_lab_problem
        :param lab_repo:
        :param lab_num_problem_num:
        :return: lab_problem
        """
        lab_problem = lab_repo.repo_search_lab_problem(lab_num_problem_num)
        return lab_problem