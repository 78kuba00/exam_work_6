from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Comment, STATUS_CHOICES
from django.http import HttpResponseRedirect
from django.urls import reverse

def index_view(request, *args, **kwargs):
    comments = Comment.objects.order_by('-created_at').filter(status='active')
    context = {
        'comments': comments
    }
    return render(request, "index.html", context)

def create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        errors = {}
        author = request.POST.get('author')
        email = request.POST.get('email')
        message = request.POST.get('message')
        status = request.POST.get('status')
        if not author:
            errors['title'] = 'Автор не может быть пустым'
        elif len(author) > 40:
            errors['title'] = 'Автор не можеть быть длиннее 40 символов'
        elif not message:
            errors['message'] = 'Комментарий не может быть пустым'
        elif len(message) > 1000:
            errors['message'] = 'Комментарий не можеть быть длиннее 3000 символов'
        elif not email:
            errors['email'] = 'Почта не может быть пустым'
        elif len(email) > 50:
            errors['email'] = 'Почта не можеть быть длиннее 50 символов'
        new_comment = Comment.objects.create(author=author, email=email, message=message, status=status)
        url = reverse('index', kwargs={'pk':new_comment.pk})
        return HttpResponseRedirect(url)
        # return HttpResponseRedirect(f'/task/{new_task.pk}/')
        # return render(request, 'task_view.html', {'task': new_task})
        # return redirect('index', pk=new_comment.pk)