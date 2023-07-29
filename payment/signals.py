from centralapp.apis.email_send import payment_success_email
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver

@receiver(valid_ipn_received)
def payment_Success(sender, **kwargs):
    print("trigger signals")
    ipn = sender
    print("INP>>>",ipn)
    if ipn.payment_status == 'Completed':
        print("status>>",ipn.payment_status)
        payment_success_email({"status":"Payment has been initiated successfully!"})

