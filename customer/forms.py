from django import forms

from .models import CustomerModel


class CustomerCreateForm(forms.ModelForm):

    class Meta:
        model = CustomerModel
        fields = ('email_address', 'first_name', 'last_name')
