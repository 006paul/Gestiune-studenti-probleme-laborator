class Grade:
    def __init__(self, student_id : int, lab_problem_num: str, grade : float | int | None = None):
        """
        Consructorul clasei Grade
        :param student_id: id-ul studentului
        :param lab_problem_num: numarul problemei de laborator
        :param grade: nota
        """
        self.__student_id = student_id
        self.__lab_problem_num = lab_problem_num
        self.__grade = grade

    @property
    def student_id(self):
        """
        Getter pentru student id
        :return: student id
        """
        return self.__student_id

    @property
    def lab_problem_num(self):
        """
        Getter pentru lab_problem_num
        :return: lab_problem_num
        """
        return self.__lab_problem_num

    @lab_problem_num.setter
    def lab_problem_num(self, lab_problem_num):
        """
        Setter pentru lab_problem_num
        :param lab_problem_num: problema de laborator
        :return: None
        """
        self.__lab_problem_num = lab_problem_num

    @property
    def grade(self):
        """
        Getter pentru grade
        :return: grade
        """
        return self.__grade

    @grade.setter
    def grade(self, grade_float):
        """
        Setter pentru grade
        :param grade_float: nota
        :return: None
        """
        grade_float = float(grade_float)
        if not (1.0 <= grade_float <= 10.0):
            raise ValueError("Nota trebuie sa fie un numar intre 1 si 10")
        self.__grade = grade_float

    def __str__(self):
        """
        Functie pentru afisarea notei unui student
        :return: ID: student id | Problema: lab_problem_num | Nota: nota_str
        """
        nota_str = f"{self.__grade}" if self.__grade is not None else "Nenotat"
        return f"ID: {self.__student_id} | Problema: {self.__lab_problem_num} | Nota: {nota_str}"

