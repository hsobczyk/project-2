from PyQt5.QtWidgets import *
from view import Ui_MainWindow

class Controller(QMainWindow, Ui_MainWindow):
    """
    A class that controls functionality of the gui
    """
    def __init__(self, *args, **kwargs):
        """
        Handles the initilization of the gui functionality.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)