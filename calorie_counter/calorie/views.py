from django.shortcuts import render, redirect
from .models import Food, Consume


def index(request):
    if request.method == 'POST':
        food_id = request.POST['food_consumed']
        food = Food.objects.get(id=food_id)
        user = request.user
        consume = Consume(user=user, food=food)
        consume.save()
        return redirect('food_list')
    foods = Food.objects.all()
    consume_foods = Consume.objects.filter(user=request.user)
    return render(request, 'index.html', {'foods':foods,'consume_foods':consume_foods })


