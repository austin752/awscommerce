from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# import stripe


# stripe.api_key = 'sk_test_isI03GLVyjFFLxEIhsaRJlIh'
STRIPE_PUB_KEY = 'pk_test_KiycWb5iEzWvmKlLY0aesms9' 


def payment_method_view(request):
    return render(request, 'billing/payment-method.html', {'publish_key': STRIPE_PUB_KEY})


def payment_method_create_view(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.POST)
        return JsonResponse({'message':'DOne'})
    return HttpResponse('error', status_code=401)
