from ticket.mappers import TicketMapper


class CustomerUnitOfWork(object):

    STATE_NEW = 'NEW'
    STATE_CLEAN = 'CLEAN'
    STATE_DIRTY = 'DIRTY'
    STATE_REMOVED = 'REMOVED'

    __mapper = None
    __storage = None
    __ticket_mapper = None
    __ticket_storage = None

    def __init__(self, mapper):
        self.__mapper = mapper
        self.__ticket_mapper = TicketMapper()

        if self.__storage is None:
            self.__storage = {}

        if self.__ticket_storage is None:
            self.__ticket_storage = {}

    def find_all(self):
        customer_entities = self.__mapper.find_all()

        for customer_entity in customer_entities:
            self.register_clean(customer_entity)

            for ticket in customer_entity.get_tickets():
                self.ticket_register_clean(ticket)

        return customer_entities

    # for debugging purposes only. remove this!
    def get_storage(self):
        return self.__storage

    # for debugging purposes only. remove this!
    def get_ticket_storage(self):
        return self.__ticket_storage

    def find_by_id(self, id):
        entity = self.__mapper.find_by_id(id)
        self.register_clean(entity)

        for ticket in entity.get_tickets():
            self.ticket_register_clean(ticket)

        return entity

    def find_by_email_address(self, email_address):
        entity = self.__mapper.find_by_email_address(email_address)
        self.register_clean(entity)

        for ticket in entity.get_tickets():
            self.ticket_register_clean(ticket)

        return entity

    def register_new(self, entity):
        self.__register_entity(entity, self.STATE_NEW)

    def ticket_register_new(self, entity):
        self.__ticket_register_entity(entity, self.STATE_NEW)

    def register_clean(self, entity):
        self.__register_entity(entity, self.STATE_CLEAN)

    def ticket_register_clean(self, entity):
        self.__ticket_register_entity(entity, self.STATE_CLEAN)

    def register_dirty(self, entity):
        self.__register_entity(entity, self.STATE_DIRTY)

    def ticket_register_dirty(self, entity):
        self.__ticket_register_entity(entity, self.STATE_DIRTY)

    def register_removed(self, entity):
        self.__register_entity(entity, self.STATE_REMOVED)

    def commit(self):
        for entity in self.__storage:
            if self.__storage[entity] == self.STATE_NEW:
                self.__mapper.create(entity)
            elif self.__storage[entity] == self.STATE_DIRTY:
                self.__mapper.update(entity)
            elif self.__storage[entity] == self.STATE_REMOVED:
                self.__mapper.delete(entity)

            for ticket_entity in entity.get_tickets():
                if self.__ticket_storage[ticket_entity] == self.STATE_NEW:
                    self.__ticket_mapper.create(ticket_entity)
                elif self.__ticket_storage[ticket_entity] == self.STATE_DIRTY:
                    self.__ticket_mapper.update(ticket_entity)
                elif self.__ticket_storage[ticket_entity] == \
                        self.STATE_REMOVED:
                    self.__ticket_mapper.delete(ticket_entity)

    def rollback(self):
        pass

    def clear(self):
        self.__storage = {}
        return self

    def __register_entity(self, entity, state):
        self.__storage[entity] = state

    def __ticket_register_entity(self, entity, state):
        self.__ticket_storage[entity] = state
