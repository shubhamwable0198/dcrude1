from django import forms
from . models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


        widgets = {

            "Delivery_Date": forms.DateInput(attrs={"type":"date","class": "form-control"})
        }