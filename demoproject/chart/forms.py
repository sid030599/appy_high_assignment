from django import forms

class date_input(forms.DateField):
    input_type= 'date'


class MyForm(forms.ModelForm):
    class Meta:
    
        widgets = {'myDateField': date_input()}
    