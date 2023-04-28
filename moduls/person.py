import time

from dataclasses import dataclass

from random import randint

from moduls.waiting_queue import WaitingQueue

from threading import Event


class Person:
    __slots__ = ('name', 'distance_km', 'priority', 'factor', 'change_point_km')

    def __init__(self, name: str, priority: int, change_point_km=1):
        self.name = name
        self.priority = priority
        self.factor = 1
        self.change_point_km = change_point_km
        self.distance_km = 0

    def __repr__(self):
        return f'Name: {self.name}, ' \
               f'Distance: {self.distance_km}, ' \
               f'Priority: {self.priority}'

    def move(self, event: Event, queue: WaitingQueue):
        """Starts the human movement. Waits for other people at the waiting point."""
        while True:
            self.distance_km += self.priority * self.factor

            if self.distance_km % self.change_point_km == 0:
                self.generate_factor()

            if self.distance_km >= queue.end_point_km:
                print(f'{self.name} has finished.')
                break

            if self.distance_km >= queue.wait_point_km:
                self.wait(event, queue)

            time.sleep(0.5)

    def generate_factor(self, start=10, end=20):
        """Sets a random value for factor."""
        self.factor = randint(start, end)

    @staticmethod
    def wait(event: Event, queue: WaitingQueue):
        """
        Blocks the movement of a person. If the number of people is equal to the total number of people, unblocks all
        people.
        """
        if queue.standby_count >= queue.persons_count - 1:
            queue.standby_count = 0
            queue.wait_point_km += queue.step_wait_point_km
            event.set()
        else:
            queue.standby_count += 1
            event.wait()
            event.clear()


@dataclass()
class Persons:
    class_person: Person
    StringVar: None


def create_persons(instance, view_path):
    """Creates a list of people."""
    instance.persons = []
    priority = 4

    for index, person in enumerate(view_path):
        instance.persons.append(Persons(Person(f'person {index}', priority), person))
        priority += 2

    instance.queue = WaitingQueue(len(instance.persons))
    instance.events = Event()
