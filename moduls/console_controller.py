from dataclasses import dataclass

from threading import Thread

from moduls.thread_handler import run_threads
from moduls.person import create_persons
from moduls.path_utils import UpdaterHandler, ConsoleUpdater


@dataclass(frozen=True)
class Commands:
    help: tuple[str, str]
    start: tuple[str, str]
    threads: tuple[str, str]
    stop: tuple[str, str, str]
    exit: tuple[str, str, str, str,]
    info: tuple[str, str]


class Console:
    __slots__ = ('threads_count', 'underway', 'show_info', 'persons', 'events', 'queue')

    COMMANDS = Commands(
        help=('/h', '/help'),
        start=('/st', '/start'),
        threads=('/t', '/threads'),
        stop=('/s', '/sp', '/stop'),
        exit=('/e', '/exit', '/q', '/quit'),
        info=('/i', '/info')
    )

    def __init__(self):
        self.threads_count = 3
        self.underway = False
        self.show_info = False
        self.persons = []
        self.events = None
        self.queue = None

    def init_threads(self):
        """The facade creates a list of people, starts streams, and displays the path."""
        create_persons(self, [None] * self.threads_count)
        run_threads(self.persons, self.events, self.queue)
        updater = UpdaterHandler(ConsoleUpdater())
        updater.init_update(self)

    def command_start(self):
        """Starts a movement of people."""
        if not self.underway:
            self.underway = True
            Thread(target=self.init_threads).start()
        else:
            print("Can't run multiple times")

    def command_stop(self):
        """Stops the movement of people."""
        if not self.underway:
            print('threads is not lunched')
        else:
            print('stop')
            self.underway = False

    def command_threads(self, input_value: str):
        """Sets the number of threads/people."""
        value = input_value.split()
        if len(value) < 2:
            print('Value error\ntry: /t 3')
        else:
            self.threads_count = int(value[1])
            print(f'threads count: {self.threads_count}')

    def command_info(self, input_value):
        """Switch to display detailed information about people."""
        value = input_value.split()
        if len(value) < 2:
            print('Value error\nCan only be "True" or "False"\ntry: /info True')
        else:
            if value[1] == 'True':
                self.show_info = True
                print('show info is True')
            elif value[1] == 'False':
                self.show_info = False
                print('show info is False')
            else:
                print('Value error\nCan only be "True" or "False')

    def init_console(self):
        """Starts command reception from the console."""
        while True:
            input_value = input('-> ')

            if input_value in self.COMMANDS.help:
                print(self.COMMANDS)
            elif input_value in self.COMMANDS.start:
                self.command_start()
            elif input_value in self.COMMANDS.exit:
                return print('exit')
            elif input_value in self.COMMANDS.stop:
                self.command_stop()
            elif (input_value[:2] or input_value[:7]) in self.COMMANDS.threads:
                self.command_threads(input_value)
            elif (input_value[:2] or input_value[:5]) in self.COMMANDS.info:
                self.command_info(input_value)
            else:
                print('Wrong command')


if __name__ == '__main__':
    Console().init_console()
