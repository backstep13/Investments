from django import forms
from django.contrib.auth.models import User

from .models import Investment, Investor


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Password don\'t match')
		return cd['password2']


class InvestmentForm(forms.ModelForm):
	class Meta:
		model = Investment
		exclude = ('investor', 'back', 'status')
		fields = ('i_type', 'interval', 'amount', 'percent')


class InvestorForm(forms.ModelForm):
	class Meta:
		model = Investor
		exclude = ('investor', 'total_invest', 'profit')
		fields = ('account', )


class BackForm(forms.ModelForm):

	class Meta:
		model = Investment
		exclude = ('investor', 'i_type', 'interval', 'amount', 'percent')
		fields = ('back', 'status')
