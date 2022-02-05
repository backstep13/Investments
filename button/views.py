from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserRegistrationForm, InvestmentForm, InvestorForm, BackForm
from .models import Investment, Investor
from .serializers import InvestmentSerializer, InvestorSerializer


def index(request):
    return render(request, "index.html")


def profile(request):
    context = Investment.objects.filter(investor=request.user.id)
    investor = Investor.objects.get(investor=request.user.id)
    return render(request, "profile.html", {'context': context, 'investor': investor})


def del_investment(request, pk):
    inv = Investment.objects.get(pk=pk)
    inv.cancel_inv()
    inv.delete()
    return redirect('profile')


def register(request):
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


def add_view(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            user = request.user
            inv = Investment()
            inv.investor = user
            inv.i_type = form.cleaned_data['i_type']
            inv.interval = form.cleaned_data['interval']
            inv.amount = form.cleaned_data['amount']
            inv.percent = form.cleaned_data['percent']
            inv.save()
            inv.save_inv()
            return redirect('profile')
    else:
        form = InvestmentForm
    return render(request, 'add.html', {'form': form})


def back_view(request, pk):
    if request.method == 'POST':
        form = BackForm(request.POST)
        if form.is_valid():
            inv = Investment.objects.get(pk=pk)
            inv.back = form.cleaned_data['back']
            inv.status = form.cleaned_data['status']
            inv.save()
            inv.back_inv()
            return redirect('profile')
    else:
        form = BackForm
    return render(request, 'back.html', {'form':form})


class AccountUpdateView(UpdateView):
    template_name = 'account.html'
    form_class = InvestorForm
    model = Investor
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.investor = self.request.user
        return super(AccountUpdateView, self).form_valid(form)


@api_view(['GET'])
def api_investment(request, pk):
    if request.method == 'GET':
        investment = Investment.objects.filter(investor=pk)
        serializer = InvestmentSerializer(investment, many=True)
        return Response(serializer.data)


class APIInvestor(APIView):
    def get(self, request, pk):
        investor = Investor.objects.get(investor=pk)
        serializer = InvestorSerializer(investor)
        return Response(serializer.data)
