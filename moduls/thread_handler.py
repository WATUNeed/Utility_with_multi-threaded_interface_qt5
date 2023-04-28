from threading import Thread, Event

from moduls.waiting_queue import WaitingQueue


def run_threads(persons: list, events: Event, queue: WaitingQueue):
    """Starts each person in a separate thread."""
    for person in persons:
        Thread(target=person.class_person.move, args=(events, queue)).start()
