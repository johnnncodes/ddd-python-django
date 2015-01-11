class UnitOfWork(object):

    STATE_NEW = 'NEW'
    STATE_CLEAN = 'CLEAN'
    STATE_DIRTY = 'DIRTY'
    STATE_REMOVED = 'REMOVED'

    __mapper = None
    __storage = None

    def __init__(self, mapper):
        self.__mapper = mapper

        if self.__storage is None:
            self.__storage = {}

    # for debugging purposes only. remove this!
    def get_storage(self):
        return self.__storage

    def find_by_id(self, id):
        entity = self.__mapper.find_by_id(id)
        self.register_clean(entity)
        return entity

    def register_new(self, entity):
        self.__register_entity(entity, self.STATE_NEW)

    def register_clean(self, entity):
        self.__register_entity(entity, self.STATE_CLEAN)

    def register_dirty(self, entity):
        self.__register_entity(entity, self.STATE_DIRTY)

    def register_removed(self, entity):
        self.__register_entity(entity, self.STATE_REMOVED)

    def commit(self):
        for entity in self.__storage:
            if self.__storage[entity] == self.STATE_NEW:
                pass
            elif self.__storage[entity] == self.STATE_DIRTY:
                self.__mapper.save(entity)
            elif self.__storage[entity] == self.STATE_REMOVED:
                self.__mapper.delete(entity)

    def rollback(self):
        pass

    def clear(self):
        self.__storage = {}
        return self

    def __register_entity(self, entity, state):
        self.__storage[entity] = state
