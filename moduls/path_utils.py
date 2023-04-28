import abc

import time


def build_path(index: int, char_index='█', char_wait='▂', char_else='▁') -> str:
    """Creates a display of the person's position and wait points."""
    result = ''
    length = 100

    for i in range(length + 1):
        if i == index:
            result = ''.join([result, char_index])
        elif i % 10 == 0:
            result = ''.join([result, char_wait])
        else:
            result = ''.join([result, char_else])

    return result


class Updater(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def update_view_path(instance):
        """Displays the path taken by all people."""
        pass

    @staticmethod
    def calculate_index(instance) -> list:
        """Calculates indices of people's position."""
        indexes = []

        for person in instance.persons:
            index = int(person.class_person.distance_km * 100 / instance.queue.end_point_km)
            limit = int(instance.queue.wait_point_km / instance.queue.end_point_km * 100)

            if index > limit:
                index = limit

            indexes.append(index)

        return indexes


class UpdaterHandler:
    def __init__(self, updater: Updater):
        self.__updater = updater

    def set_strategy(self, updater: Updater):
        self.__updater = updater

    def init_update(self, instance):
        self.__updater.update_view_path(instance)


class UIUpdater(Updater):
    @staticmethod
    def update_view_path(instance):
        instance.textbox.delete("0.0")
        indexes = Updater.calculate_index(instance)

        for person, index in zip(instance.persons, indexes):
            instance.textbox.insert("0.0", text=f'{build_path(index)}\n\n')


class Qt5Updater(Updater):
    @staticmethod
    def update_view_path(instance):
        indexes = Updater.calculate_index(instance)

        for person, index in zip(instance.progress_view_list, indexes):
            person.setText(build_path(index))


class ConsoleUpdater(Updater):
    @staticmethod
    def update_view_path(instance):
        print('\n')
        while True:
            indexes = Updater.calculate_index(instance)

            for person, index in zip(instance.persons, indexes):
                print(build_path(index))

            if instance.show_info:
                stats = ''.join(f'{e.class_person.name}\t'
                                f'in {e.class_person.distance_km}\t'
                                f'priority: {e.class_person.priority}\n' for e in instance.persons)
                stats = ''.join([stats, f'wait point: {instance.queue.wait_point_km}',
                                 f'\tend point: {instance.queue.end_point_km}'])

                print(stats)
            print()

            if all(person.class_person.distance_km >= instance.queue.end_point_km for person in instance.persons):
                return

            if not instance.underway:
                instance.underway = False
                return

            time.sleep(1)
