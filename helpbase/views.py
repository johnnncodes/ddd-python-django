from django.views.generic import ListView

from customer.unit_of_work import CustomerUnitOfWork
from customer.hydrators import CustomerHydrator


class HomeView(ListView):

    template_name = 'helpbase/home.html'

    def get_queryset(self):
        session = CustomerUnitOfWork()
        return CustomerHydrator().extract(session.find_all(), True)
