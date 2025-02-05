from django.shortcuts import render,redirect, get_object_or_404
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