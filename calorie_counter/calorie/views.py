from django.shortcuts import render, redirect,get_object_or_404
# from django.contrib.auth.decorators import login_required
from .models import Food, Consume

# @login_required
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


def delete_consume(request, id):
    consumed_food = get_object_or_404(Consume, id=id, user=request.user)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('food_list')
    return render(request, 'delete.html')