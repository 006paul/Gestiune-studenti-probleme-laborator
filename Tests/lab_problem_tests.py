from Business.lab_problem_services import LabProblemService
from Domain.grade import Grade
from Domain.lab_problem import LabProblem
from datetime import date

from Repository.grades_list import GradeRepository
from Repository.lab_problem_list import LabProblemRepository
from Validations.lab_problem_validations import LabProblemValidations


class LabProblemTests:
    def test_lab_problem(self):
        """
        Functie care testeaza clasa LabProblem si getters pt LabProblem
        :return: None
        """
        lab_problem = LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17))
        assert lab_problem.lab_num_problem_num == "lab1-p2"
        assert lab_problem.description == "A doua problema"
        assert lab_problem.deadline == date(2027, 11, 17)

    def test_lab_problem_setters(self):
        """
        Functie care testeaza setters pt LabProblem
        :return: None
        """
        lab_problem = LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17))
        lab_problem.lab_num_problem_num = "lab1-p3"
        lab_problem.description = "A treia problema"
        lab_problem.deadline = date(2028, 11, 17)
        assert lab_problem.lab_num_problem_num == "lab1-p3"
        assert lab_problem.description == "A treia problema"
        assert lab_problem.deadline == date(2028, 11, 17)

    def test_lab_repo(self):
        """
        Functie care testeaza clasa LabProblemRepository si getters LabProblemRepository
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        assert len(test_lab_repo_list.lab_problems) == 3
        assert test_lab_repo_list.lab_problems[1].description == "Prima problema"

    def test_repo_add_lab_problem(self):
        """
        Functie care testeaza repo_add_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        lab_problem = LabProblem("lab3-p1", "l3p1", date(2027, 11, 17))
        test_lab_repo_list.repo_add_lab_problem(lab_problem)
        assert test_lab_repo_list.lab_problems[3].description == "l3p1"

    def test_repo_remove_lab_problem(self):
        """
        Functie care testeaza repo_remove_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        test_lab_repo_list.repo_remove_lab_problem("lab2-p3")
        assert len(test_lab_repo_list.lab_problems) == 2

    def test_add_lab_problem(self):
        """
        Functie care testeaza add_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        test_lab_p = LabProblem("lab3-p1", "l3p1", date(2027, 11, 17))
        LabProblemService().add_lab_problem(test_lab_repo_list, test_lab_p.lab_num_problem_num, test_lab_p.description, test_lab_p.deadline)
        assert len(test_lab_repo_list.lab_problems) == 4

    def test_remove_lab_problem(self):
        """
        Functie care testeaza remove_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        test_grades_repo = test_grades_repo = GradeRepository([
            Grade(1, "lab1-p1", 9.5),
            Grade(2, "lab1-p1", 8.0)
        ])
        LabProblemService().remove_lab_problem(test_lab_repo_list, test_grades_repo, "lab2-p3")
        assert len(test_lab_repo_list.lab_problems) == 2

    def test_validate_lab_problem_num(self):
        """
        Functie care testeaza validate_lab_problem_num
        :return: None
        """
        try:
            LabProblemValidations().validate_lab_problem_num("lab-p")
            assert False
        except ValueError:
            assert True

    def test_validate_lab_problem(self):
        """
        Functie care testeaza validate_lab_problem
        :return: None
        """
        lab_p = LabProblem("lab-p1", "l3p1", date(2027, 11, 17))
        try:
            LabProblemValidations().validate_lab_problem(lab_p)
            assert False
        except ValueError:
            assert True

    def test_modify_lab_problem(self):
        """
        Functie care testeaza modify_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        test_grades_repo = GradeRepository([
            Grade(1, "lab1-p1", 9.5),
            Grade(2, "lab1-p1", 8.0)])
        LabProblemService().modify_lab_problem(test_lab_repo_list, test_grades_repo, "lab2-p3", "lab3-p2", "problema 2", date(2028, 11, 17))
        assert test_lab_repo_list.lab_problems[2].description == "problema 2"

    def test_repo_modify_lab_problem(self):
        """
        Functie care testeaza repo_modify_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        lab_problem = LabProblem("lab2-p2", "A doua problema lab2", date(2027, 11, 17))
        test_lab_repo_list.repo_modify_lab_problem("lab1-p2", lab_problem)
        assert test_lab_repo_list.lab_problems[0].description == "A doua problema lab2"

    def test_repo_search_lab_problem(self):
        """
        Functie care testeaza repo_search_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        searched_lab_problem = test_lab_repo_list.repo_search_lab_problem("lab1-p2")
        assert test_lab_repo_list.lab_problems[0] == searched_lab_problem

    def test_search_lab_problem(self):
        """
        Functie care testeaza search_lab_problem
        :return: None
        """
        test_lab_repo_list = LabProblemRepository([LabProblem("lab1-p2", "A doua problema", date(2027, 11, 17)),
                                                   LabProblem("lab2-p1", "Prima problema", date(2027, 12, 17)),
                                                   LabProblem("lab2-p3", "A treia problema", date(2028, 11, 17))])
        searched_lab_problem = LabProblemService().search_lab_problem(test_lab_repo_list, "lab1-p2")
        assert test_lab_repo_list.lab_problems[0] == searched_lab_problem

    def run_all_lab_problem_tests(self):
        """
        Functie care ruleaza toate testele pt problemele de laborator
        :return: None
        """
        self.test_lab_problem()
        self.test_lab_problem_setters()
        self.test_lab_repo()
        self.test_repo_add_lab_problem()
        self.test_repo_remove_lab_problem()
        self.test_add_lab_problem()
        self.test_remove_lab_problem()
        self.test_validate_lab_problem_num()
        self.test_validate_lab_problem()
        self.test_modify_lab_problem()
        self.test_repo_modify_lab_problem()
        self.test_repo_search_lab_problem()
        self.test_search_lab_problem()
