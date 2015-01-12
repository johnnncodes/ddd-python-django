class TicketHydrator(object):

    def __extract(self, ticket):
        extracted_ticket = {
            'uuid': ticket.get_uuid(),
            'title': ticket.get_title(),
            'body': ticket.get_body()
        }
        return extracted_ticket

    def hydrate(self):
        pass

    def extract(self, ticket_or_tickets, many=False):
        if many:
            extracted_tickets = []
            for ticket in ticket_or_tickets:
                extracted_ticket = self.__extract(ticket)
                extracted_tickets.append(extracted_ticket)
            return extracted_tickets
        else:
            extracted_ticket = self.__extract(ticket)
            return extracted_ticket
