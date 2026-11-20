class Student:
    def __init__(self, id_student: int, name: str, group: int):
        """
        Constructorul clasei Student
        :param id_student: ID-ul studentului
        :param name: numele studentului
        :param group: grupa studentului
        """
        self.__id_student = id_student
        self.__name = name
        self.__group = group

    @property
    def id_student(self):
        """
        Getter pentru id_student
        :return: __id_student
        """
        return self.__id_student

    @property
    def name(self):
        """
        Getter pentru name
        :return:
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Setter pentru name
        :param name: numele name care trebuie setat
        :return: None
        """
        if not name or name.strip() == "":
            raise ValueError("Numele nu poate fi vid")
        elif not all(c.isalpha() or c.isspace() for c in name):
            raise ValueError("Numele poate sa contina doar spatiu")
        else:
            self.__name = name

    @property
    def group(self):
        """
        Getter pentru group
        :return: __group
        """
        return self.__group

    @group.setter
    def group(self, group):
        """
        Setter pentru group
        :param group: gupa care trebuie setata
        :return: None
        """
        if group < 0:
            raise ValueError("Grupa trebuie sa fie un numar pozitiv")
        else:
            self.__group = group

    def __str__(self):
        """
        Functie folosita la afisarea datelor unui student
        :return:
        """
        return f"ID: {self.id_student} | Nume: {self.name} | Grupa: {self.group}"

    def __repr__(self):
        """
        Functie folosita la afisarea datelor unui student in lista
        :return:
        """
        pass