class LabProblemRepository:
    def __init__(self, lab_problem_list):
        """
        Constructorul pentru clasa LabProblemRepository
        :param lab_problem_list: lista de probleme de laborator
        """
        self.__lab_problem_list = lab_problem_list

    def repo_add_lab_problem(self, lab_problem):
        for p in self.__lab_problem_list:
            if p.lab_num_problem_num == lab_problem.lab_num_problem_num:
                raise ValueError("Problema exista deja")
        self.__lab_problem_list.append(lab_problem)

    def repo_remove_lab_problem(self, lab_problem_num):
        for p in self.__lab_problem_list:
            if p.lab_num_problem_num == lab_problem_num:
                self.__lab_problem_list.remove(p)
                return

    @property
    def lab_problems(self):
        """
        Getter pentru lista de probleme de laborator
        :return: lab_problem_list - lista de probleme de laborator
        """
        return self.__lab_problem_list