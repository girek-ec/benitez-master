from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@shared_task
def payment_completed(order_id):
    """
    Tarea para enviar una notificación por correo electrónico cuando se realiza un pedido pagado exitosamente.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f'Vortice Store - Pedido No. {order.id}'
    message = 'Por  favor, encuentre  adjunto el pedido  de  su  compra  reciente'
    email = EmailMessage(subject,
                         message,
                         'vortice.ec@gmail.com',
                         [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                          stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()
