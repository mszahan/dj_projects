from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            # return render(request, 'create_post.html', {'form': form})
    else:
        form = PostCreateForm()
    return render(request, 'create_post.html', {'form': form})




