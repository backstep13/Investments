from django import forms
from django.contrib.auth.models import User

from .models import Investment, Investor


class UserRegistrationForm(forms.ModelForm):
	"""Form for registration users
	with confirm password. if passwords not equal send a message """
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Пароль не совпадает')
		return cd['password2']


class InvestmentForm(forms.ModelForm):
	"""Form of input investment data"""
	class Meta:
		model = Investment
		exclude = ('investor', 'back', 'status')
		fields = ('i_type', 'interval', 'amount', 'percent')


class InvestorForm(forms.ModelForm):
	"""Form to change of investor's money amount"""
	class Meta:
		model = Investor
		exclude = ('investor', 'total_invest', 'profit')
		fields = ('account', )


class BackForm(forms.ModelForm):
	"""Form to back money from investment"""
	class Meta:
		model = Investment
		exclude = ('investor', 'i_type', 'interval', 'amount', 'percent')
		fields = ('back', 'status')
