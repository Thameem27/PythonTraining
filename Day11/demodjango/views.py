from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def greetTheUser(request):
    return HttpResponse("Welcome to the Magic of Django")