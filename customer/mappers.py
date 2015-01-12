from customer.models import CustomerModel
from customer.entities import Customer
from ticket.mappers import TicketMapper
from helpbase.mappers import AbstractDataMapper
from customer.value_objects import EmailAddress


class CustomerMapper(AbstractDataMapper):

    def find_all(self):
        customer_models = CustomerModel.objects.all()

        customer_entities = []
        for customer_model in customer_models:
            ticket_entities = TicketMapper().get_by_customer_id(
                customer_model.uuid)
            customer_entity = self.__load_entity(
                customer_model, ticket_entities)
            customer_entities.append(customer_entity)
        return customer_entities

    def find_by_id(self, id):
        customer_model = CustomerModel.objects.get(uuid=id)
        ticket_entities = TicketMapper().get_by_customer_id(id)
        customer = self.__load_entity(customer_model, ticket_entities)
        return customer

    def find_by_email_address(self, email_address):
        customer_model = CustomerModel.objects.get(email_address=email_address)
        ticket_entities = TicketMapper().get_by_customer_id(
            customer_model.uuid)
        customer = self.__load_entity(customer_model, ticket_entities)
        return customer

    def create(self, customer):
        CustomerModel(
            uuid=customer.get_uuid(),
            email_address=customer.get_email_address(),
            first_name=customer.get_first_name(),
            last_name=customer.get_last_name()
        ).save()

    def update(self, customer):
        customer_model = CustomerModel.objects.get(uuid=customer.get_uuid())
        customer_model.first_name = customer.get_first_name()
        customer_model.last_name = customer.get_last_name()
        customer_model.email_address = customer.get_email_address()
        customer_model.save()

    def delete(self, entity):
        print 'implement delete'

    def __load_entity(self, customer_model, ticket_entities):
        customer_entity = Customer(
            customer_model.uuid,
            EmailAddress(customer_model.email_address),
            customer_model.first_name,
            customer_model.last_name,
            ticket_entities
        )
        return customer_entity
