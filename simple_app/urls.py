from django.urls import path

from simple_app.views import (
    ShowItem,
    buy_item,
    successful_payment,
    cancel_payment
)

urlpatterns = [
    path('item/<int:pk>', ShowItem.as_view(template_name='item.html'), name='item'),
    path('buy/<item_id>', buy_item, name='buy_item'),
    path('successful_payment/', successful_payment, name='successful_payment'),
    path('cancel_payment/', cancel_payment, name='cancel_payment'),
]
