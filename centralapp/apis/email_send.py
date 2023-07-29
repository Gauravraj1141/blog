from django.core.mail import EmailMessage
from django.template.loader import get_template

from django.conf import settings
EMAIL_ADMIN  = settings.EMAIL_HOST_USER


def send_email_to_sales(request):
    customer_detail = request
    message = get_template("emailtemplate/sales_email_template.html").render({
        'data': customer_detail
    })
    mail = EmailMessage(
        subject=f"New Customer Inquiry - {customer_detail['name']}",
        body=message,
        from_email=EMAIL_ADMIN,
        to=["sales@novusaurelius.com"],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    return mail.send()


def send_email_to_customer_service(request):
    customer_detail = request
    message = get_template("emailtemplate/customer_service_email_template.html").render({
        'data': customer_detail
    })
    mail = EmailMessage(
        subject= f"New Complaint from {customer_detail['name']}",
        body=message,
        from_email=EMAIL_ADMIN,
        to=["customerservice@novusaurelius.com"],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    return mail.send()

def send_otp_to_user(request):
    customer_detail = request
    print(customer_detail)
    message = get_template("emailtemplate/send_otp_to_user_email_template.html").render({
        'data': customer_detail
    })
    mail = EmailMessage(
        subject= f"Email Verification - {customer_detail['otp']}",
        body=message,
        from_email=EMAIL_ADMIN,
        to=[customer_detail['email']],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    return mail.send()


def payment_success_email(request):
    customer_detail = request
    message = get_template("emailtemplate/payment_success_email.html").render({
        'data': customer_detail
    })
    mail = EmailMessage(
        subject= f"Email Verification for Successfull Payment",
        body=message,
        from_email=EMAIL_ADMIN,
        to=["gaurav@mailinator.com"],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    return mail.send()