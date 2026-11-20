class GradeValidations:
    def validate_grade(self, grade : float |int):
        if not (1.0 <= grade <= 10.0):
            raise ValueError("Nota trebuie sa fie un numar intre 1 si 10")