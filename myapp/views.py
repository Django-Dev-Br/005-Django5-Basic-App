from django.http import HttpResponse

def example_view(request):
    return HttpResponse("app up and running properly")
