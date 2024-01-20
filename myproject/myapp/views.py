from django.http import HttpResponse
from .models import Country , City

def add_record(request):
    e = Country.objects.all()
    print(e)
    return HttpResponse("Hello, world. You're at the polls mustapha .")

