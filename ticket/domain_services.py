import uuid

from customer.entities import Customer
from customer.models import CustomerModel
from customer.unit_of_work import CustomerUnitOfWork
from helpbase.exceptions import InvalidInputsException
from customer.value_objects import EmailAddress
from customer.forms import CustomerCreateForm
from ticket.value_objects import Title
from ticket.forms import TicketCreateForm


class TicketCreateService(object):

    __customer_create_form = None
    __ticket_create_form = None

    def run(
        self,
        email_address,
        first_name,
        last_name,
        title,
        body
    ):
        inputs = {
            'email_address': email_address,
            'first_name': first_name,
            'last_name': last_name,
            'title': title,
            'body': body
        }

        ticket_create_form = TicketCreateForm(inputs)
        customer_create_form = CustomerCreateForm(inputs)

        self.__ticket_create_form = ticket_create_form
        self.__customer_create_form = customer_create_form

        if customer_create_form.is_valid() and ticket_create_form.is_valid():
            session = CustomerUnitOfWork()

            try:
                customer = session.find_by_email_address(email_address)
                ticket = customer.create_ticket(Title(title), body)
                session.ticket_register_new(ticket)
            except CustomerModel.DoesNotExist:
                customer = Customer(
                    uuid.uuid4(),
                    EmailAddress(email_address),
                    first_name,
                    last_name
                )
                session.register_new(customer)
                ticket = customer.create_ticket(
                    Title(title),
                    body
                )
                session.ticket_register_new(ticket)
            session.commit()
        else:
            raise InvalidInputsException

    def get_form(self):
        return (self.__customer_create_form, self.__ticket_create_form)
