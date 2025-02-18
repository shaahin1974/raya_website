from django.shortcuts import render

from .models import ServiceArea


def index(request):
    service_listings = ServiceArea.objects.filter(is_published=True)[:3]

    context = {
        'service_listings': service_listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def team(request):
    return render(request, 'pages/team.html')
