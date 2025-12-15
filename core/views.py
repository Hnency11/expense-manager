from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Sum
from django.utils import timezone
from .models import Transaction, Category, Budget
from .forms import TransactionForm, BudgetForm
import json

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    today = timezone.now()
    transactions = Transaction.objects.filter(user=request.user)
    
    # Monthly summaries
    current_month_transactions = transactions.filter(date__year=today.year, date__month=today.month)
    income = current_month_transactions.filter(type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    expenses = current_month_transactions.filter(type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expenses
    
    recent_transactions = transactions.order_by('-date', '-created_at')[:5]

    # Chart Data
    expense_by_category = current_month_transactions.filter(type='EXPENSE').values('category__name').annotate(total=Sum('amount'))
    chart_labels = [item['category__name'] for item in expense_by_category if item['category__name']]
    chart_data = [float(item['total']) for item in expense_by_category]
    
    context = {
        'income': income,
        'expenses': expenses,
        'balance': balance,
        'recent_transactions': recent_transactions,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(request.user)
    return render(request, 'transaction_form.html', {'form': form, 'title': 'Add Transaction'})

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transaction_list.html', {'transactions': transactions})

@login_required
def manage_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.user, request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('manage_budgets')
    else:
        form = BudgetForm(request.user)
    return render(request, 'manage_budgets.html', {'budgets': budgets, 'form': form})
