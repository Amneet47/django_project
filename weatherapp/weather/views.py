import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=290a6cebf4762da8c80a4dca7dabf341&units=metric"
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        
        result = requests.get(url.format(city)).json()
    
        city_weather = {
            'city': city.name,
            'temperature': result['main']['temp'],
            'description': result['weather'][0]['description'],
            'icon': result['weather'][0]['icon']
        }
        
        weather_data.append(city_weather)
    
    context = {
        'weather_data': weather_data,
        'form': form
    }
    return render(request, 'weather/weather.html', context)