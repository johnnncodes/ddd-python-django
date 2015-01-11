class InvalidTitleException(Exception):
    pass


class Title(object):

    __value = None

    def __init__(self, value):
        if value:
            self.__value = value
        else:
            raise InvalidTitleException

    def __repr__(self):
        return self.__value
