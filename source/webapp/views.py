from django.shortcuts import render
from webapp.models import Comment

def index_view(request, *args, **kwargs):
    comments = Comment.objects.order_by('-created_at').filter(status='active')
    context = {
        'comments': comments
    }
    return render(request, "index.html", context)

# Create your views here.
