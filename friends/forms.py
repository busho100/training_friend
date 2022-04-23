from django import forms

class HelloForm(forms.Form):
    ''' id = forms.IntegerField(label='ID') '''

    name = forms.CharField(label='氏名',\
        widget=forms.TextInput(attrs={'class':'form-control'}))

    mail = forms.EmailField(label = 'Ｅメール',\
        widget=forms.EmailInput(attrs={'class':'form-control'}))

    male = forms.BooleanField(label = '性別', required=False,\
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))

    age = forms.IntegerField(label = '年齢',\
        widget=forms.NumberInput(attrs={'class':'form-control'}))

    birthday = forms.DateField(label = '誕生日',\
        widget=forms.DateInput(attrs={'class':'form-controle'}))