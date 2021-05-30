import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from covetgroup import forms
from covetgroup.helpers import mail

from wsgiref.util import FileWrapper
from mysite.settings import STATIC_DIR

from django.contrib import messages


# Create your views here.
@cache_page(60 * 60 * 24)  # Cache the page for 24 hours
def index(request):
    form = forms.SubscribeToPDF()

    if request.method == "POST":
        form = forms.SubscribeToPDF(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, f"E-Mail erfolgreich gesendet!")
            pdf_file = os.path.join(STATIC_DIR, "media", "KDB_INNEN_240x288_200710.pdf")
            mail.send_pdf(request.POST['email'], pdf_file)
            form = forms.SubscribeToPDF()

    return render(request, 'our-brands.html', {'form': form})


# def download_pdf(request):
#     filename = os.path.join(STATIC_DIR, "media", "KDB_INNEN_240x288_200710.pdf")
#     wrapper = FileWrapper(open(filename, 'rb'))
#     response = HttpResponse(wrapper, content_type='application/force-download')
#     response['Content-Length'] = os.path.getsize(filename)
#     response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
#
#     return response

@cache_page(60 * 60 * 24)  # Cache the page for 24 hours
def impressum(request):
    return render(request, 'impressum.html')


@cache_page(60 * 60 * 24)  # Cache the page for 24 hours
def datenschutz(request):
    return render(request, 'datenschutz.html')
