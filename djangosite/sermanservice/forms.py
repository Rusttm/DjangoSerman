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


class ParsingForm(Form):

    report_types = ( ('Choose site for parsing', 'Choose site for parsing'),
                     ('All sites parsing', 'All sites parsing'),
                     ('Serman site', 'Serman site'),
                     ('Forest site', 'Forest site'),
                     ('Pakt site', 'Pakt site'),
                     ('Cascad site', 'Cascad site'),
                     )

    type_report = forms.ChoiceField(choices=report_types)

