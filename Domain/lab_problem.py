from datetime import date

class LabProblem:
    def __init__(self, lab_num_problem_num: str, description: str, deadline: date):
        """
        Constructorul pentru clasa LabProblem
        :param lab_num_problem_num:
        :param description:
        :param deadline:
        """
        self.__lab_num_problem_num = lab_num_problem_num
        self.__description = description
        self.__deadline = deadline

    @property
    def lab_num_problem_num(self):
        """
        Getter pentru lab_num_problem_num
        :return: lab_num_problem_num
        """
        return self.__lab_num_problem_num

    @lab_num_problem_num.setter
    def lab_num_problem_num(self, lab_num_problem_num):
        """
        Setter pentru lab_num_problem_num
        :param lab_num_problem_num: lab_num_problem_num care trebuie setat
        :return: None
        """
        self.__lab_num_problem_num = lab_num_problem_num

    @property
    def description(self):
        """
        Getter pentru description
        :return: description
        """
        return self.__description

    @description.setter
    def description(self, description):
        """
        Setter pentru description
        :param description: description care trebuie setat
        :return: None
        """
        self.__description = description

    @property
    def deadline(self):
        """
        Getter pentru deadline
        :return: deadline
        """
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline):
        """
        Setter pentru deadline
        :param deadline: deadline care trebuie setat
        :return: None
        """
        self.__deadline = deadline

    def __str__(self):
        """
        Functie pentru afisearea datelor unei probleme de laborator
        :return:
        """
        return f"Numar: {self.__lab_num_problem_num}, Descriere: {self.__description}, Deadline: {self.__deadline.strftime('%d/%m/%Y')}"