from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockData
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

import requests
import json


APIKEY = 'B8K18TXAK2ZXRDPW' 


#if False, the app will always query the Alpha Vantage APIs regardless of whether the stock data for a given ticker is already in the local database
DATABASE_ACCESS = True 



def test(request):
    # Return JSON data of the users in the database
    users = User.objects.all()
    return JsonResponse(list(users.values()), safe=False)



@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {})


@csrf_exempt
def get_stock_data(request):
    if request.is_ajax():
        #get ticker from the AJAX POST request
        ticker = request.POST.get('ticker', 'null')
        ticker = ticker.upper()

        if DATABASE_ACCESS == True:
            #checking if the database already has data stored for this ticker before querying the Alpha Vantage API
            if StockData.objects.filter(symbol=ticker).exists(): 
                #We have the data in our database! Get the data from the database directly and send it back to the frontend AJAX call
                entry = StockData.objects.filter(symbol=ticker)[0]
                return HttpResponse(entry.data, content_type='application/json')

        #obtain stock data from Alpha Vantage APIs
        #get adjusted close data
        price_series = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={APIKEY}&outputsize=full').json()
        
        #get SMA (simple moving average) data
        sma_series = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=close&apikey={APIKEY}').json()

        #package up the data in an output dictionary 
        output_dictionary = {}
        output_dictionary['prices'] = price_series
        output_dictionary['sma'] = sma_series

        #save the dictionary to database
        temp = StockData(symbol=ticker, data=json.dumps(output_dictionary))
        temp.save()

        #return the data back to the frontend AJAX call 
        return JsonResponse(output_dictionary)

    else:
        message = "Not Ajax"
        return HttpResponse(message)
    


from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def save_user_info(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the user information to the database
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserForm()

    return render(request, 'registration.html', {'form': form})

from django.contrib.auth.views import LoginView, LogoutView

# Login view
class MyLoginView(LoginView):
    template_name = 'login.html'

# Logout view
class MyLogoutView(LogoutView):
    # Optionally, you can specify a URL to redirect to after logout
    next_page = 'login'  # Change 'login' to the URL name of your login view

