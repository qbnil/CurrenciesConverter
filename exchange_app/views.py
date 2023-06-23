from django.shortcuts import render, redirect
import requests
from .forms import RegistrationForm
from .models import Currency


def exchange(request):
    # Retrieve the latest currency rates from the API
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    # Update or save the currency rates to the database
    for currency_name, currency_rate in currencies.items():
        # Check if the currency rate is valid before updating/saving
        if currency_rate is not None:
            currency, created = Currency.objects.get_or_create(name=currency_name)
            if created or currency.rate != currency_rate:
                currency.rate = currency_rate
                currency.save()


    if request.method == 'GET':
        context = {
            'currencies': currencies.keys(),
        }
        return render(request=request, template_name='exchange_app/index.html', context=context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        # Retrieve the converscion rate from the database
        from_currency = Currency.objects.get(name=from_curr)
        to_currency = Currency.objects.get(name=to_curr)
        conversion_rate = to_currency.rate / from_currency.rate

        converted_amount = round(conversion_rate * from_amount, 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'converted_amount': converted_amount,
            'currencies': currencies.keys(),
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)
