import abc


class AbstractDataMapper(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def find_all(self):
        return

    @abc.abstractmethod
    def find_by_id(self, id):
        return

    @abc.abstractmethod
    def create(self):
        return

    @abc.abstractmethod
    def update(self):
        return

    @abc.abstractmethod
    def delete(self):
        return
