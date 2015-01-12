from ticket.models import TicketModel
from ticket.entities import Ticket
from ticket.value_objects import Title
from helpbase.mappers import AbstractDataMapper


class TicketMapper(AbstractDataMapper):

    def find_all(self):
        pass

    def find_by_id(self, customer_id):
        pass

    def create(self, ticket):
        TicketModel(
            uuid=ticket.get_uuid(),
            title=ticket.get_title(),
            body=ticket.get_body(),
            customer_uuid=ticket.get_customer_id()
        ).save()

    def update(self, ticket):
        ticket_model = TicketModel.objects.get(uuid=ticket.get_uuid())
        ticket_model.title = ticket.get_title()
        ticket_model.body = ticket.get_body()
        ticket_model.save()

    def delete(self):
        pass

    def get_by_customer_id(self, customer_id):
        ticket_models = TicketModel.objects.filter(customer_uuid=customer_id)

        ticket_entities = []
        for ticket_model in ticket_models:
            ticket_entity = self.__load_entity(ticket_model)
            ticket_entities.append(ticket_entity)
        return ticket_entities

    def __load_entity(self, ticket_model):
        ticket_entity = Ticket(
            ticket_model.uuid,
            Title(ticket_model.title),
            ticket_model.body,
            ticket_model.customer_uuid
        )
        return ticket_entity
