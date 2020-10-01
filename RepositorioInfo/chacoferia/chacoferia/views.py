from django.http import HttpResponse


# una vista
def bienvenida(request):
    return HttpResponse("Bienvenido a django....")


