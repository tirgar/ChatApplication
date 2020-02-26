"""
    create at Feb 26/2020 by mjghasepmour (topcoder-mc)
    - this package is interface of observers
"""
class Observer:
    
    def notification(self, message):
        """ Receive update from subject
            :params message: incoming message
        """
        pass
