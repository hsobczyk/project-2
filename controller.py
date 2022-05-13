from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import sys
import datetime

from schedule_launch import *

class Controller(QMainWindow, Ui_MainWindow):
    """
    A class that controls functionality of the gui
    """

    def __init__(self, *args, **kwargs):
        """
        Handles the initilization of the gui functionality.
        """
        super().__init__(*args, **kwargs)
        self.setFixedSize(812, 559)
        self.setupUi(self)
        self.exit_button.clicked.connect(lambda : self.exit())
        self.run_button.clicked.connect(lambda : self.run())
        self.submit_input_button.clicked.connect(lambda : self.submit())

    def exit(self) -> None:
        """
        Function that exits the program
        """
        sys.exit()

    def run(self) -> None:
        """
        Function that will run the threads if at least one thread exists.
        Will disable all new thread inputs.
        """
        if launcher_threads[0]:
            self.hours_input.setEnabled(False)
            self.minutes_input.setEnabled(False)
            self.seconds_input.setEnabled(False)
            self.filename_input.setEnabled(False)
            self.submit_input_button.setEnabled(False)
            self.run_button.setEnabled(False)
            run_threads()

    def clear(self) -> None:
        """
        Clears the input boxes
        """
        self.hours_input.setValue(0)
        self.minutes_input.setValue(0)
        self.seconds_input.setValue(0)
        self.filename_input.setText('')

    threadCounts = 0
    def submit(self) -> None:
        """
        Takes the time and filename and adds it to a thread
        """
        filename = r'{}'.format(self.filename_input.text())
        hour = int(self.hours_input.text())
        minute = int(self.minutes_input.text())
        second = int(self.seconds_input.text())
        delta_str = str(delta_creator(ihours=hour, iminutes=minute, iseconds=second))

        if self.threadCounts < 5:
            thread_creator(filename, datetime.timedelta(seconds=second))

        if self.threadCounts==0:
            self.output_filename_0.setText(filename)
            self.output_time_0.setText(delta_str)
        elif self.threadCounts==1:
            self.output_filename_1.setText(filename)
            self.output_time_1.setText(delta_str)
        elif self.threadCounts==2:
            self.output_filename_2.setText(filename)
            self.output_time_2.setText(delta_str)
        elif self.threadCounts==3:
            self.output_filename_3.setText(filename)
            self.output_time_3.setText(delta_str)
        elif self.threadCounts==4:
            self.output_filename_4.setText(filename)
            self.output_time_4.setText(delta_str)

        self.clear()
        self.threadCounts+=1