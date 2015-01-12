class UnitOfWork(object):

    STATE_NEW = 'NEW'
    STATE_CLEAN = 'CLEAN'
    STATE_DIRTY = 'DIRTY'
    STATE_REMOVED = 'REMOVED'

    _mapper = None
    _storage = None

    def __init__(self, mapper):
        self._mapper = mapper

        if self._storage is None:
            self._storage = {}

    def find_all(self):
        entities = self._mapper.find_all()

        for entity in entities:
            self.register_clean(entity)

        return entities

    def find_by_id(self, id):
        entity = self._mapper.find_by_id(id)
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
        for entity in self._storage:
            if self._storage[entity] == self.STATE_NEW:
                self._mapper.create(entity)
            elif self._storage[entity] == self.STATE_DIRTY:
                self._mapper.update(entity)
            elif self._storage[entity] == self.STATE_REMOVED:
                self._mapper.delete(entity)

    # TODO: implement this
    def rollback(self):
        pass

    def clear(self):
        self._storage = {}
        return self

    def __register_entity(self, entity, state):
        self._storage[entity] = state
