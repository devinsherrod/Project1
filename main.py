from PyQt6.QtWidgets import QMainWindow, QApplication
from Project1GUI import Ui_MainWindow
from Project1Logic import VotingBallots
import sys

class BallotQApp(QMainWindow):
    """
    Main application window for the voting system.
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.voter = VotingBallots()
        self.ui.Submit_button.clicked.connect(self.handle_submit)

    def handle_submit(self):
        """
        deals with all submit button antics.
        :return:
        """
        voter_id = self.ui.ID_input.text().strip()

        candidate = ''
        if self.ui.Jane_button.isChecked():
            candidate = 'JANE'
        elif self.ui.John_button.isChecked():
            candidate = 'JOHN'
        elif self.ui.Bill_button.isChecked():
            candidate = 'BILL'

        feedback = self.voter.validation_votes(voter_id, candidate)
        self.ui.Feedback_label.setText(feedback)
        if feedback == 'Vote Successful':
            self.ui.ID_input.clear()
            self.ui.Jane_button.setChecked(False)
            self.ui.John_button.setChecked(False)
            self.ui.Bill_button.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BallotQApp()
    window.show()
    sys.exit(app.exec())
