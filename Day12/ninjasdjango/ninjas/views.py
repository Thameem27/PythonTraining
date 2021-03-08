from django.shortcuts import render, get_object_or_404
from .models import Developer
# Create your views here.
def index(request):
    dev_list = Developer.objects.all()
    context = {
        'dev_list': dev_list
    }
    return render(request, 'ninjas/index.html', context)

def details(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    return render(request, 'ninjas/details.html', {'dev':dev})