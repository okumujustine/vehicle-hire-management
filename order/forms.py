from django import forms

from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'title',
            'description',
            'number_of_vehicles',
            'number_of_days',
            'customer',
            'status',
            'from_location',
            'to_location',
            'unit_of_masurement',
            'initial_start_date',
            'initial_end_date',
            'budget_amount_or_cost',
            'updated_start_date',
            'updated_end_date',
        )
        exclude = ('currency', 'company', 'created_by', 'updated_by')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['updated_start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['updated_end_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['initial_start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['initial_end_date'].widget = forms.DateInput(attrs={'type': 'date'})
