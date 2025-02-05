import datetime
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Sum
from .forms import ExpenseForm
from .models import Expense


def index(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('homepage')
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
    
    #logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    #data is greater than last year
    last_year_expense = Expense.objects.filter(date__gt=last_year)
    yearly_sum = last_year_expense.aggregate(Sum('amount'))
    
    #logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    #data is greater than last year
    last_month_expense = Expense.objects.filter(date__gt=last_month)
    monthly_sum = last_month_expense.aggregate(Sum('amount'))
    
    #logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    #data is greater than last year
    last_week_expense = Expense.objects.filter(date__gt=last_week)
    weekly_sum = last_week_expense.aggregate(Sum('amount'))

    expense_form = ExpenseForm()
    return render(request,'index.html', {'expense_form':expense_form, 
                                         'expenses':expenses, 
                                         'total_expenses':total_expenses,
                                         'yearly_sum':yearly_sum,
                                         'monthly_sum':monthly_sum,
                                         'weekly_sum':weekly_sum,
                                         })


def edit(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('homepage')
    return render(request, 'edit.html', {'expense_form':expense_form})

def delete(request, id):
    # just to make sure the delete is in the post method since two post method in same page
    if request.method == 'POST' and 'delete' in request.POST:
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        return redirect('homepage')