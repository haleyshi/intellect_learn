"""
https://github.com/nemonik/Intellect
"""

import sys, logging, time, random
from intellect.Intellect import Intellect
from BuyOrder import BuyOrder

class MyIntellect(Intellect):
    pass


if __name__ == "__main__":
    logger = logging.getLogger('intellect')
    logger.setLevel(logging.ERROR)
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)

    logger = logging.getLogger('example')
    logger.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)

    logging.getLogger('example').debug("Creating reasoning engine.")
    myIntellect = MyIntellect()

    logging.getLogger('example').debug("Asking the engine to learn my policy.")
    policy = myIntellect.learn(myIntellect.local_file_uri("./rulesets/example.policy"))

    max_buy_orders_to_start = input('Provide the maximum number possible buy orders to start with: ')
    buy_order_to_start = random.randint(1, max_buy_orders_to_start)

    logging.getLogger('example').debug("Asking the engine to learn a BuyOrder for {0} sheep.".format(buy_order_to_start))
    myIntellect.learn(BuyOrder(buy_order_to_start))

    myIntellect.reason()

    while True:
        logging.getLogger('example').debug("{0} in knowledage.".format(myIntellect.knowledge))
        time.sleep(5)
        logging.getLogger('example').debug("Messaging reasoning engine to reason.")
        myIntellect.reason()