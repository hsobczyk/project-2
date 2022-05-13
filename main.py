# Original Idea: https://automatetheboringstuff.com/2e/chapter17/
from controller import *


def main():

    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
