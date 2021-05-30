from django.core import mail


def send_pdf(receiver, attachment=None):
    sender = "info@kaiserdicke.de"
    subject = "Kaiser & Dicke"
    message = "Vielen Dank für Ihr Interesse"
    email = mail.EmailMessage(
        subject, message, sender, [receiver])

    if attachment:
        email.attach_file(attachment)

    email.send()
