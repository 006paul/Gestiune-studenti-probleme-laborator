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
        return self.__student_id

    @property
    def lab_problem_num(self):
        return self.__lab_problem_num

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade_float):
        self.__grade = grade_float

    def __str__(self):
        nota_str = f"{self.__grade}" if self.__grade is not None else "Nenotat"
        return f"ID: {self.__student_id} | Problema: {self.__lab_problem_num} | Nota: {nota_str}"

