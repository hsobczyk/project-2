# Original Idea: https://automatetheboringstuff.com/2e/chapter17/
# added gui, and the ability to add to a list
from controller import *


def main():

    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
