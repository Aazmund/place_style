from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
                           label='',
                           required=True,
                           error_messages={'required': ''}
                           )
    number = forms.CharField(max_length=12,
                             widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
                             label='',
                             required=True,
                             error_messages={'required': ''}
                             )
    choice = forms.ChoiceField(choices=(
                                        (1, "Курсы фермеров"),
                                        (2, "Курсы по каркасному строительству домов"),
                                        (3, "Курсы кузнецов"), (4, "Курсы прорабов"), (5, "Курсы антиквариата"),
                                        (6, "Курсы печников"), (7, "Курсы по обучению электромонтажу")),
                               label='',
                               error_messages={'required': ''}
                               )


class NumberForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
                           label='',
                           required=True,
                           error_messages={'required': ''},
                           )
    number = forms.CharField(max_length=12,
                             widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
                             label='',
                             required=True,
                             error_messages={'required': ''}
                             )