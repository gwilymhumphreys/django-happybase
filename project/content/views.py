from django.shortcuts import render, get_object_or_404
from models import *


def home(request):
    """
    A simple home page
    """
    context = {
        'pages': Page.objects.all(),
    }
    return render(request, 'index.html', context)


def page(request, slug):
    """
    A simple content page
    """
    page = get_object_or_404(Page, slug=slug)

    context = {
        'page': page,
    }

    return render(request, 'page.html', context)
