def validate_student(student):
    """
    Functie care valideaza un student student
    :param student: studentul care trebuie validat
    :return: lista de erori
    """
    errors = []
    if student.id_student < 0:
        errors.append("ID-ul trebuie sa fie un numar pozitiv")
    if not student.name or student.name.strip() == "":
        errors.append("Numele nu poate fi vid")
    if not all(c.isalpha() or c.isspace() for c in student.name):
        errors.append("Numele poate sa contina doar litere si spatiu")
    if student.group < 0:
        errors.append("Grupa trebuie sa fie un numar pozitiv")
    if len(errors) > 0:
        raise ValueError("\n".join(errors))

def validate_id(repo, student_id):
    """
    Functie care valideaza daca ID-ul student_id se afla in repo
    :param repo: lista de studenti
    :param student_id: ID-ul care se valideaza
    :return: None
    """
    ok = False
    for student in repo.students:
        if student.id_student == student_id:
            ok = True

    if not ok:
        raise ValueError("Studentul nu exista")
