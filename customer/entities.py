import uuid

from ticket.entities import Ticket
from customer.value_objects import EmailAddress


class Customer(object):
    __uuid = None
    __email_address = None
    __first_name = None
    __last_name = None
    __tickets = None  # list of tickets

    def __init__(
        self,
        uuid,
        email_address,
        first_name,
        last_name,
        tickets=None
    ):

        if not isinstance(email_address, EmailAddress):
            raise Exception

        self.set_uuid(uuid)
        self.set_email_address(email_address)
        self.set_first_name(first_name)
        self.set_last_name(last_name)

        if tickets is None:
            tickets = []

        self.__tickets = tickets

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_email_address(self):
        return self.__email_address

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def create_ticket(self, title, body):
        ticket = Ticket(uuid.uuid4(), title, body, self.get_uuid())
        if self.__tickets is None:
            self.__tickets = []
        self.__tickets.append(ticket)
        return ticket

    def get_tickets(self):
        return self.__tickets

    def find_ticket_by_id(self, id):
        for ticket in self.get_tickets():
            if ticket.get_uuid().hex == id:
                return ticket

    def close_ticket(self, ticket):
        ticket.close()
        return ticket

    def set_uuid(self, uuid):
        self.__uuid = uuid

    def get_uuid(self):
        return self.__uuid
