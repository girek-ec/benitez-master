from django.urls import path
from . import views
from . import webhooks
from .views import payment_process, payment_completed, payment_canceled, send_whatsapp_and_email, orden_pedido

app_name = 'payment'

urlpatterns = [
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),


    path('process/', payment_process, name='process'),
    path('completed/', payment_completed, name='completed'),
    path('canceled/', payment_canceled, name='canceled'),
    path('send-whatsapp-email/', send_whatsapp_and_email, name='send_whatsapp_email'),
    path('orden_pedido/', orden_pedido, name='orden pedido'),

]

