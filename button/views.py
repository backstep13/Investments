from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .forms import UserRegistrationForm, InvestmentForm, InvestorForm, BackForm
from .models import Investment, Investor
from .serializers import InvestmentSerializer


class Index(TemplateView):
    """Start page"""
    template_name = 'index.html'


def register(request):
    """User Registration"""
    user_form = UserRegistrationForm(request.POST)

    if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        user = User.objects.get(username=user_form.cleaned_data['username'])
        Investor.objects.create(investor=user)
        return render(request, "registration/register_done.html", {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/register.html", {'user_form': user_form})


class Profile(TemplateView):
    """If user is authenticated show him a profile page
    else start page"""
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usr = self.request.user.id
        if usr is not None:
            context['context'] = Investment.objects.filter(investor=usr)
            context['investor'] = Investor.objects.get(investor=usr)
            return context
        else:
            return redirect('index')


class AddView(CreateView):
    """Class add investment to DB from special form"""
    template_name = 'add.html'
    form_class = InvestmentForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.investor = self.request.user
        inv = Investment()
        inv.i_type = form.cleaned_data['i_type']
        inv.interval = form.cleaned_data['interval']
        inv.amount = form.cleaned_data['amount']
        inv.percent = form.cleaned_data['percent']
        inv.save()
        inv.save_inv()
        return super(AddView, self).form_valid(form)


class BackView(UpdateView):
    """Function changes status of investment if it closed,
    from special form """
    template_name = 'back.html'
    form_class = BackForm
    model = Investment
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        inv = Investment.objects.get(pk=self.object.pk)
        inv.back = form.cleaned_data['back']
        inv.status = form.cleaned_data['status']
        inv.save()
        inv.back_inv()
        return super(BackView, self).form_valid(form)


class DelView(DeleteView):
    """Delete investment by the user"""
    model = Investment
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inv = Investment.objects.get(pk=self.object.pk)
        inv.cancel_inv()
        inv.delete()
        return context


class AccountUpdateView(UpdateView):
    """Class help to change of money amount of the investor
     from special form"""
    template_name = 'account.html'
    form_class = InvestorForm
    model = Investor
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.investor = self.request.user
        return super(AccountUpdateView, self).form_valid(form)


# API classes
class APIInvestment(ModelViewSet):
    """API for get, post, put, delete methods.
    Work with JSON data, have filters, search, ordering and perm."""
    serializer_class = InvestmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['amount']
    search_fields = ['interval', 'percent']
    ordering_fields = ['percent', 'amount']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Permission for authenticated users"""
        user = self.request.user
        return Investment.objects.filter(investor=user)
