"""
    create at Feb 26/2020 by mjghasepmour (topcoder-mc)
    - this package is interface of observer's subjects handler
"""

from abc import ABC, abstractmethod
from .observer import Observer


class Subject(ABC):
    """
        the subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer):
        """ Attach an observer to the subject """
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """
            Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self):
        """ Notify all observers about an event. """
        pass
