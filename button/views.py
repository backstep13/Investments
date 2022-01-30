from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import UserRegistrationForm, InvestmentForm, InvestorForm
from .models import Investment, Investor


def index(request):
    return render(request, "index.html")

def profile(request):
    context = Investment.objects.filter(investor=request.user.id)
    investor = Investor.objects.get(investor=request.user.id)

    return render(request, "profile.html", {'context': context, 'investor': investor})

def register(request):
    user_form = UserRegistrationForm(request.POST)

    if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return render(request, "registration/register_done.html", {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/register.html", {'user_form': user_form})

class AddCreateView(CreateView):
    template_name = 'add.html'
    form_class = InvestmentForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.investor = self.request.user
        return super(AddCreateView, self).form_valid(form)

class AccountCreateView(CreateView):
    template_name = 'account.html'
    form_class = InvestorForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.investor = self.request.user
        return super(AccountCreateView, self).form_valid(form)
