from django.shortcuts import render, redirect
from django.views.generic import View

from customer.forms import CustomerCreateForm
from ticket.forms import TicketCreateForm
from ticket.domain_services import TicketCreateService
from helpbase.exceptions import InvalidInputsException


class TicketCreateView(View):

    def get(self, request, *args, **kwargs):
        ticket_create_form = TicketCreateForm()
        customer_create_form = CustomerCreateForm()

        return render(
            request,
            'ticket/create.html',
            {
                'ticket_create_form': ticket_create_form,
                'customer_create_form': customer_create_form
            }
        )

    def post(self, request, *args, **kwargs):
        email_address = request.POST.get('email_address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        ticket_title = request.POST.get('title')
        ticket_body = request.POST.get('body')

        ticketCreateService = TicketCreateService()

        try:
            ticketCreateService.run(
                email_address,
                first_name,
                last_name,
                ticket_title,
                ticket_body
            )
            return redirect('home')
        except InvalidInputsException:
            customer_create_form, ticket_create_form = \
                ticketCreateService.get_form()
            return render(
                request,
                'ticket/create.html',
                {
                    'ticket_create_form': ticket_create_form,
                    'customer_create_form': customer_create_form
                }
            )
