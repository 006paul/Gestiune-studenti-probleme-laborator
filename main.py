from Repository.lab_problem_list import LabProblemRepository
from Repository.students_list import StudentsRepository
from Tests.lab_problem_tests import LabProblemTests
from Tests.student_tests import StudentsTests
from UI.ui import UI


def main():
    """
    Functie care porneste aplicatia
    :return: None
    """
    StudentsTests().run_all_student_tests()
    LabProblemTests().run_all_lab_problem_tests()
    repo = StudentsRepository([])
    lab_repo = LabProblemRepository([])

    while True:
        UI().ui_menu()
        command = UI().ui_get_command()
        if command == "exit":
            exit()
        UI().ui_run_console(command, repo, lab_repo)


if __name__ == "__main__":
    main()
