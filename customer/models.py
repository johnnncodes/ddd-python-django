from django.db import models

from uuidfield import UUIDField


class CustomerModel(models.Model):

    uuid = UUIDField(primary_key=True, auto=False)

    # TODO: set unique to True and just override it on the form
    # since we want the form to be valid even if the email address
    # already exists in the database. The mapper will be responsible for
    # making sure that there will be no duplicated email addresses in the db.
    # We still want to set unique=True in the model though just to make sure.
    email_address = models.EmailField(max_length=254, unique=False)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
