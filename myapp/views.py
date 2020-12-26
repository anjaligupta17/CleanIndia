from django.shortcuts import render, HttpResponse
from myapp.models import contactModel
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable": "this is sent",
        "variable2": "this is anji website"
    }

    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is aboutpage")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is servicepage")


def contact(request):
    if request.method == "POST":
        Email = request.POST.get('email')
        Query = request.POST.get('query')
        print(Email)
        print(Query)
        c1 = contactModel()
        c1.Email = Email
        c1.Query = Query
        c1.save()
        messages.success(request, 'Your messages been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("this is contactpage")
