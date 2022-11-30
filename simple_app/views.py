import stripe
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.conf import settings
from simple_app.models import Item
from django.urls import reverse


def successful_payment(request):

    return HttpResponse('OK')


def cancel_payment(request):

    return HttpResponse('CANCEL')


class ShowItem(DetailView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = context['item']
        context['stripe_api_key'] = settings.STRIPE_API_KEY
        return context


def buy_item(request, item_id):
    stripe.api_key = settings.STRIPE_API_KEY
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.get_currency_display(),
                'product_data': {
                    'name': f'Ваш заказ {item.name}',
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('successful_payment')
        ),
        cancel_url=request.build_absolute_uri(
            reverse('cancel_payment')
        ),
    )
    return JsonResponse({'sessionId': session['id']})


def get_home_page(request):
    items = Item.objects.all()
    return render(request, 'home.html', context={'items': items})
