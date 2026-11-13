from Repository.lab_problem_list import LabProblemRepository
from Repository.students_list import StudentsRepository
from Tests.student_tests import run_all_student_tests
from UI.ui import ui_run_console, ui_get_command, ui_menu


def main():
    """
    Functie care porneste aplicatia
    :return: None
    """
    run_all_student_tests()
    repo = StudentsRepository([])
    lab_repo = LabProblemRepository([])
    while True:
        ui_menu()
        command = ui_get_command()
        if command == "exit":
            exit()
        ui_run_console(command, repo, lab_repo)

if __name__ == "__main__":
    main()
