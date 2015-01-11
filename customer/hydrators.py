from ticket.hydrators import TicketHydrator


class CustomerHydrator(object):

    def __extract(self, customer, tickets):
        extractedCustomer = {
            'uuid': customer.get_uuid(),
            'email_address': customer.get_email_address(),
            'first_name': customer.get_first_name(),
            'last_name': customer.get_last_name(),
            'tickets': tickets
        }
        return extractedCustomer

    def hydrate(self):
        pass

    def extract(self, customerOrcustomers, many=False):
        if many:
            extractedCustomers = []
            for customer in customerOrcustomers:
                tickets = TicketHydrator().extract(
                    customer.get_tickets(), True)
                extractedCustomer = self.__extract(customer, tickets)
                extractedCustomers.append(extractedCustomer)
            return extractedCustomers
        else:
            tickets = TicketHydrator().extract(customer.get_tickets(), True)
            extractedCustomer = self.__extract(customer, tickets)
            return extractedCustomer
