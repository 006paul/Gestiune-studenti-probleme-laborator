from Domain.lab_problem import LabProblem


class LabProblemRepository:
    def __init__(self, lab_problem_list):
        """
        Constructorul pentru clasa LabProblemRepository
        :param lab_problem_list: lista de probleme de laborator
        """
        self.__lab_problem_list = lab_problem_list

    def repo_add_lab_problem(self, lab_problem : LabProblem):
        for p in self.__lab_problem_list:
            if p.lab_num_problem_num == lab_problem.lab_num_problem_num:
                raise ValueError("Problema exista deja")
        self.__lab_problem_list.append(lab_problem)

    def repo_remove_lab_problem(self, lab_problem_num):
        for p in self.__lab_problem_list:
            if p.lab_num_problem_num == lab_problem_num:
                self.__lab_problem_list.remove(p)
                return
        raise ValueError("Problema nu exista")

    @property
    def lab_problems(self):
        """
        Getter pentru lista de probleme de laborator
        :return: lab_problem_list - lista de probleme de laborator
        """
        return self.__lab_problem_list

    def repo_modify_lab_problem(self, p_to_modify: str, lab_problem: LabProblem):
        if p_to_modify != lab_problem.lab_num_problem_num:
            for p in self.__lab_problem_list:
                if p.lab_num_problem_num == lab_problem.lab_num_problem_num:
                    raise ValueError("Exista deja o problema cu acest numar")

        for p in self.__lab_problem_list:
            if p.lab_num_problem_num == p_to_modify:
                p.lab_num_problem_num = lab_problem.lab_num_problem_num
                p.description = lab_problem.description
                p.deadline = lab_problem.deadline
                return
        raise ValueError("Problema nu exista")

    def repo_search_lab_problem(self, lab_num_problem_num):
        """
        Functie care cauta o problema de laborator
        :param lab_num_problem_num: numarul problemei cautate
        :return: lab_problem
        """
        for p in self.__lab_problem_list:
            if p.lab_num_problem_num == lab_num_problem_num:
                return p
        raise ValueError("Problema nu exista")