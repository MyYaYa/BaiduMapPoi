import signal
from .log import logger

class SignalProcess():

    def __init__(self):
        self.is_interrupt = False
        signal.signal(signal.SIGINT, self.sigint_handler)

    def sigint_handler(self, sig_num, frame):
        self.is_interrupt = True
        logger.info("!!!!!!!! SIGINT is received !!!!!!!!")
