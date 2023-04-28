from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import sys
from moduls.gui import design_ui

from moduls.person import create_persons
from moduls.thread_handler import run_threads
from moduls.path_utils import UpdaterHandler, Qt5Updater

import platform

import subprocess


class App(QtWidgets.QMainWindow, main_ui.Ui_lab1):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        self.start_btn.clicked.connect(self.init_threads)
        self.console_btn.clicked.connect(self.create_console)

        self.progress_view_list = [self.progress_bars_layout.itemAt(i).widget()
                                   for i in range(self.progress_bars_layout.count())]

        self.persons = []
        self.events = None
        self.queue = None

        self.updater = UpdaterHandler(Qt5Updater())
        self.init_update()
        timer_per_seconds = QTimer(self, interval=1000, timeout=self.init_update).start()

    @staticmethod
    def create_console():
        """Creates a console in a new subprocess."""
        if platform.system() == 'Windows':
            subprocess.Popen('cmd.exe /c python console_controller.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(['gnome-terminal', '-e', 'python ./console_controller.py'])

    def init_update(self):
        """Starts the update of the trip display."""
        self.updater.init_update(instance=self)
        self.update()

    def init_threads(self):
        """Starts each person in a separate thread."""
        create_persons(self, self.progress_view_list)
        run_threads(self.persons, self.events, self.queue)


def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
