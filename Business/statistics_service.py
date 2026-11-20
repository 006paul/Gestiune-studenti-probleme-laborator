class StatisticsService:
    def sort_students_and_grades_by_name(self, repo):
        """
        Functie care sorteaza studentii din repo in ordine alfabetica
        :param repo: lista de studenti
        :return: sorted_repo - lista cu studentii sortati
        """
        sorted_repo = repo.students.copy()
        sorted_repo.sort(key=lambda x: (x.name.lower(), x.id_student))
        return sorted_repo

    def sort_students_by_grade(self, repo, grades_repo, problem):
        """
        Functie care sorteaza studentii in ordinea descrescatoare a notelor
        :param repo: lista de studenti
        :param grades_repo: lista de note
        :param problem: problema de laborator la care se sorteaza notele
        :return: sorted_repo - lista cu studentii sortati
        """
        students_with_grades = []
        for student in repo.students:
            grade = next((g for g in grades_repo.grades
                          if g.student_id == student.id_student
                          and g.lab_problem_num == problem), None)
            if grade is not None:
                students_with_grades.append((student, grade))
        students_with_grades.sort(
            key=lambda item: item[1].grade if item[1].grade is not None else float("-inf"),
            reverse=True
        )
        return students_with_grades

    def students_with_average_less_than_five(self, repo, grades_repo):
        students_with_average = []

        for student in repo.students:
            num_grades = 0
            average_grade = 0
            for grade in grades_repo.grades:
                if grade.student_id == student.id_student:
                    if grade.grade is not None:
                        average_grade += grade.grade
                        num_grades += 1
            if num_grades != 0:
                average_grade = average_grade / num_grades
                students_with_average.append((student, average_grade))
        students_with_average = [(student, average_grade) for student, average_grade in students_with_average
                                 if average_grade < 5]
        return students_with_average

