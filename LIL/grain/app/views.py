from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, welcome to the Grain Products Store!</h1>")
