from ticket.value_objects import Title


class Ticket(object):
    __uuid = None
    __title = None
    __body = None
    __customer_id = None

    def __init__(self, uuid, title, body, customer_id):
        if not isinstance(title, Title):
            raise Exception

        self.set_uuid(uuid)
        self.set_title(title)
        self.set_body(body)
        self.set_customer_id(customer_id)

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def set_uuid(self, uuid):
        self.__uuid = uuid

    def get_uuid(self):
        return self.__uuid

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_id(self):
        return self.__customer_id

    def close(self):
        pass
