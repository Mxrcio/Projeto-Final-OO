from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Cliente', widget=forms.TextInput(attrs={'required': 'required'}))
    feedback = forms.CharField(widget=forms.Textarea(attrs={'required': 'required'}))
    rating = forms.ChoiceField(choices=[
        ('5', 'Excelente'),
        ('4', 'Bom'),
        ('3', 'Regular'),
        ('2', 'Ruim'),
        ('1', 'Péssimo'),
    ], widget=forms.RadioSelect(attrs={'required': 'required'}))
