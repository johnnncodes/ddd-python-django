from django.views.generic import ListView

from customer.mappers import CustomerMapper
from customer.unit_of_work import CustomerUnitOfWork
from customer.hydrators import CustomerHydrator


class HomeView(ListView):

    template_name = 'helpbase/home.html'

    def get_queryset(self):
        session = CustomerUnitOfWork(CustomerMapper())
        return CustomerHydrator().extract(session.find_all(), True)
