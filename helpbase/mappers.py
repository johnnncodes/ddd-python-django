import abc


class AbstractDataMapper(object):
    __metaclass__ = abc.ABCMeta

    # TODO: add required methods here

    @abc.abstractmethod
    def find_by_id(self, id):
        return
