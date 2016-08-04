import logging, time
import thread, random
from threading import Lock
from BagOfWool import BagOfWool

def grow_wool(sheep):
    while True:

        time.sleep(random.randint(2, 5))

        logging.getLogger("example").debug("{0}: Grew a bag of wool.".format(sheep.name))
        sheep.bags_of_wool.append(BagOfWool())

        if len(sheep.bags_of_wool) == 3:
            logging.getLogger("example").debug("{0}: Waiting around for retirement.".format(sheep.name))
            break

class BlackSheep():
    '''
        Used to signify a black sheep
    '''

    number = 0

    def __init__(self):
        '''
        BlackSheep Initializer
        '''
        self.bags_of_wool = []
        BlackSheep.number = BlackSheep.number + 1
        self.name = "Sheep #{0}".format(BlackSheep.number)

        logging.getLogger("example").debug("Creating {0}.".format(self.name))

        self.lock = Lock()
        thread.start_new_thread(grow_wool, (self,))


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def bags_of_wool(self):
        return self._bags_of_wool

    @bags_of_wool.setter
    def bags_of_wool(self, value):
        self.lock.acquire()
        self._bags_of_wool = value
        self.lock.release()


if __name__ == '__main__':
    sheep = BlackSheep()

    while True:
        time.sleep(5)
        print len(sheep.bags_of_wool)

        if len(sheep.bags_of_wool) == 3:
            break