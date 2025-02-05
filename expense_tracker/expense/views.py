from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense


def index(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('homepage')
    expenses = Expense.objects.all()
    expense_form = ExpenseForm()
    return render(request,'index.html', {'expense_form':expense_form, 'expenses':expenses})