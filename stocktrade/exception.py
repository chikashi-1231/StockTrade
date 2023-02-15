import logging

class BatchError(Exception):
    
    def __init__(self, message):
        self.err_message = message

    def __str__(self):
        logging.error(self.err_message)