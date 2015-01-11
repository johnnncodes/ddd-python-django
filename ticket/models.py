from uuidfield import UUIDField

from django.db import models


class TicketModel(models.Model):

    uuid = UUIDField(primary_key=True, auto=False)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    customer_uuid = UUIDField(auto=False)
