from django.http import HttpResponse
from django.shortcuts import render



def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse("Данные отправлены!")
    return render(request,'students/contact.html' )
