
import logging

class BuyOrder(object):

    def __init__(self, count=1):
        logging.getLogger("example").debug("Creating buy order for {0} sheep.".format(count))

        self.count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value