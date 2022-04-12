import logging

"""
This is base class script for all the errors that can be used to log error and raise custom error

"""


class PkgError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)

    def __str__(self):
        if self.message:
            msg = f'{type(self).__name__}, {self.message}'
        else:
            msg = f'{type(self).__name__} has been raised.'
        self._logger.exception(msg)
        return msg
