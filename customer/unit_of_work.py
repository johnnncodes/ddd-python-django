from ticket.mappers import TicketMapper
from helpbase.unit_of_work import UnitOfWork
from customer.mappers import CustomerMapper


class CustomerUnitOfWork(UnitOfWork):

    __ticket_mapper = None
    __ticket_storage = None

    def __init__(self):
        super(CustomerUnitOfWork, self).__init__(CustomerMapper())

        # TODO: check if we can set __ticket_mapper = TicketMapper()
        # directly at the top?
        self.__ticket_mapper = TicketMapper()

        if self.__ticket_storage is None:
            self.__ticket_storage = {}

    def find_all(self):
        customer_entities = super(CustomerUnitOfWork, self).find_all()

        for customer_entity in customer_entities:
            for ticket in customer_entity.get_tickets():
                self.ticket_register_clean(ticket)

        return customer_entities

    def find_by_id(self, id):
        entity = super(CustomerUnitOfWork, self).find_by_id(id)

        for ticket in entity.get_tickets():
            self.ticket_register_clean(ticket)

        return entity

    def find_by_email_address(self, email_address):
        entity = self._mapper.find_by_email_address(email_address)
        self.register_clean(entity)

        for ticket in entity.get_tickets():
            self.ticket_register_clean(ticket)

        return entity

    def ticket_register_new(self, entity):
        self.__ticket_register_entity(entity, self.STATE_NEW)

    def ticket_register_clean(self, entity):
        self.__ticket_register_entity(entity, self.STATE_CLEAN)

    def ticket_register_dirty(self, entity):
        self.__ticket_register_entity(entity, self.STATE_DIRTY)

    def commit(self):
        super(CustomerUnitOfWork, self).commit()
        for entity in self._storage:
            for ticket_entity in entity.get_tickets():
                if self.__ticket_storage[ticket_entity] == self.STATE_NEW:
                    self.__ticket_mapper.create(ticket_entity)
                elif self.__ticket_storage[ticket_entity] == self.STATE_DIRTY:
                    self.__ticket_mapper.update(ticket_entity)
                elif self.__ticket_storage[ticket_entity] == \
                        self.STATE_REMOVED:
                    self.__ticket_mapper.delete(ticket_entity)

    def __ticket_register_entity(self, entity, state):
        self.__ticket_storage[entity] = state
