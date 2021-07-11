from django import forms
from django.forms import Form, ModelForm, DateField, widgets



class ReportForm(Form):
    report_types = ( ('AccountSum', 'AccountSum'),
    ('Sales taxbook', 'Sales taxbook'),
    ('Purchases taxbook', 'Purchases taxbook'),
    ('Profit report', 'Profit report'),
    ('Agents report', 'Agents report'),
    )
    holder_types = (('Main', 'Main'),('Nsk', 'Nsk'),('Pfo', 'Pfo'),)
    type_report = forms.ChoiceField(choices=report_types)
    from_date = DateField(label="From Date", widget=widgets.DateInput(attrs={'type': 'date'}))
    to_date = DateField(label="To Date", widget=widgets.DateInput(attrs={'type': 'date'}))
    type_holder = forms.ChoiceField(choices=holder_types)

class ReportForm2(ModelForm):

    report_types = ( ('AccountSum', 'AccountSum'),
    ('Sales taxbook', 'Sales taxbook'),
    ('Purchases taxbook', 'Purchases taxbook'),
    ('Profit report', 'Profit report'),
    ('Agents report', 'Agents report'),
    )
    holder_types = (('Main', 'Main'),('Nsk', 'Nsk'),('Pfo', 'Pfo'),)
    type_report = forms.ChoiceField(choices=report_types)
    from_date = DateField(label="From Date", widget=widgets.DateInput(attrs={'type': 'date'}))
    to_date = DateField(label="To Date", widget=widgets.DateInput(attrs={'type': 'date'}))
    type_holder = forms.ChoiceField(choices=holder_types)
