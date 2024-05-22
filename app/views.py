from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kathmandu'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978'
    param = {'units':'metric'}

    try:
        data = requests.get(url,param).json()

        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']

        context = {
            'temp':temp,
            'desc':desc,
            'icon':icon,
            'wind':wind,
            'humidity':humidity
        }

        return render(request,'index.html',context=context)

    except:
        temp = '0'
        desc = 'No data found.'
        icon = ''
        wind = '0'
        humidity = '0'

        context = {
            'temp':temp,
            'desc':desc,
            'icon':icon,
            'wind':wind,
            'humidity':humidity
        }

        return render(request,'index.html',context=context)