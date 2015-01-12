from ticket.hydrators import TicketHydrator


class CustomerHydrator(object):

    def __extract(self, customer, tickets):
        extracted_customer = {
            'uuid': customer.get_uuid(),
            'email_address': customer.get_email_address(),
            'first_name': customer.get_first_name(),
            'last_name': customer.get_last_name(),
            'tickets': tickets
        }
        return extracted_customer

    def hydrate(self):
        pass

    def extract(self, customer_or_customers, many=False):
        if many:
            extracted_customers = []
            for customer in customer_or_customers:
                tickets = TicketHydrator().extract(
                    customer.get_tickets(), True)
                extracted_customer = self.__extract(customer, tickets)
                extracted_customers.append(extracted_customer)
            return extracted_customers
        else:
            tickets = TicketHydrator().extract(customer.get_tickets(), True)
            extracted_customer = self.__extract(customer, tickets)
            return extracted_customer
