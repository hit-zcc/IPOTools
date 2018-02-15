from abc import ABCMeta, abstractclassmethod

from base.exception import FormateException
from base.Queue import Queue


class InputBase:
    __metaclass__ = ABCMeta
    __connection__ = None
    __inputFormate__ = None

    def init(self, connection):
        self.__connection__ = connection

    def InjectInputFormate(self, inputFormate):
        if self.__connection__:
            raise FormateException.InputFormateInsException
        self.__inputFormate__ = inputFormate

    def LetIn(self):
        for index, line in enumerate(self.__connection__.getFormateResult()):
            Queue.putMessage(index, line)

    @abstractclassmethod
    def getFormateResult(self):
        pass
