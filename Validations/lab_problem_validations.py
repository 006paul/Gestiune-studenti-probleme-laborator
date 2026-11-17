from datetime import date

class LabProblemValidations:
    def validate_lab_problem_num(self, lab_problem_num):
        """
        Functie care valideaza corectitudinea formatului pentru lab_num_problem_num
        :param lab_problem: problema de laborator
        :return: None
        """
        errors = []
        parts = lab_problem_num.split("-")
        if not len(parts) == 2 or not parts[0].startswith("lab") or not parts[1].startswith("p"):
            raise ValueError("Format gresit pentru labX-pY")
        lab_str = parts[0][3:]
        p_str = parts[1][1:]

        if not lab_str.isdigit() or not int(lab_str) > 0:
            errors.append("Numarul laboratorului trebuie sa fie numar natural")
        if not p_str.isdigit() or not int(p_str) > 0:
            errors.append("Numarul problemei trebuie sa fie numar natural")
        if len(errors) > 0:
            raise ValueError("\n".join(errors))

    def validate_lab_problem(self, lab_problem):
        """
        Functie care valideaza problema de laborator lab_problem
        :param lab_problem: problema de laborator
        :return: None
        """
        errors = []
        self.validate_lab_problem_num(lab_problem.lab_num_problem_num)
        if not lab_problem.description.strip():
            errors.append("Descrierea nu poate fi vida")

        if lab_problem.deadline < date.today():
            errors.append("Deadline-ul nu poate fi in trecut")

        if len(errors) > 0:
            raise ValueError("\n".join(errors))

