
from interfaces.observer_pattern.subject import Subject
from interfaces.observer_pattern.observer import Observer
from utils.singleton import singleton

from typing import Set


@singleton
class ConcentrateSubject(Subject):
    # main parent
    
    _observers: Set = set()
    
    def attach(self, observer: Observer):
        """ Attach an observer to the subject
            :params observer: get new observer class
        """
        for item in self._observers:
            if item.class_name == observer.class_name:
                return
        self._observers.add(observer)

    def detach(self, observer: Observer):
        """
            Detach an observer from the subject.
        """
        self._observers.discard(observer)

    def notify(self, message, to):
        """ Notify all observers about an event. """
        for observer in self._observers:
            if observer.class_name == to:
                observer.notification(message)
