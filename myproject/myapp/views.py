from django.http import HttpResponse
from .models import Country , City,record
from django.http import JsonResponse

def add_record(request):
    countries_list = Country.objects.all().values()
    #get cities 

    #get records
    data = {}
    for country in countries_list:
        c = Country.objects.get(name = country['name'])
        ref_city = City.objects.filter(country = c).all()
        k = {}
        for _ref_city in ref_city:
            f = {_ref_city.name:[]}
            records  = record.objects.filter(city=_ref_city).all()
            for _record in records:
                f[_ref_city.name].append(_record.name)
                k = {**k, **f}
        data[c.name] = k
    response = JsonResponse(data)
    return response

