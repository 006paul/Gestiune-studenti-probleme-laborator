class StudentsRepository:
    def __init__(self, students_list):
        """
        Constructorul clasei StudentsRepository
        :param students_list: lista de studenti
        """
        self.__students_list = students_list

    def repo_add_student(self, student):
        """
        Functie care adauga un student in lista de studenti
        :param student: studentul care se adauga in lista
        :return: None
        """
        for s in self.__students_list:
            if s.id_student == student.id_student:
                raise ValueError("Studentul exista deja")
        self.__students_list.append(student)

    def repo_remove_student(self, student_id):
        """
        Functie care sterge un student cu ID-ul student_id din repo
        :param student_id: ID-ul studentului care este sters
        :return: None
        """
        for s in self.__students_list:
            if s.id_student == student_id:
                self.__students_list.remove(s)
                return

    @property
    def students(self):
        """
        Getter pentru lista de studenti
        :return: __students_list - lista de studenti
        """
        return self.__students_list


