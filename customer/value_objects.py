import re


class InvalidEmailAddressException(Exception):
    pass


class EmailAddress(object):

    __email_address = None

    def __init__(self, email_address):
        if re.match(r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', email_address, re.IGNORECASE):
            self.__email_address = email_address
        else:
            raise InvalidEmailAddressException

    def __repr__(self):
        return self.__email_address
