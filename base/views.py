from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.shortcuts import redirect

def index(request):
    services = Service.objects.all()
    return render(
        request,
        "index.html",
        {
            "services": services,
            "numberData": NumberData.objects.all(),
            "team": Director.objects.all(),
            "testi": Testimonial.objects.all(),
        },
    )
def add_email(request):
    print(request.POST.get("email"))
    if 'email' in request.POST:
        if not Email.objects.filter(email=request.POST.get("email")).exists():
            print(request.POST.get("email"))
            Email.objects.create(email=request.POST.get("email"))
            return JsonResponse({"status": True, 'email': request.POST.get("email"), 'status': 200}, status=200)
    return JsonResponse({"status": False, 'status': 400}, status=400)
def service_list(request, id):
    services = Service.objects.all()
    service = Service.objects.get(id=id)
    return render(
        request, "service-list.html", {"service": service, "services": services}
    )
def service_sub_list(request, id):
    services = Service.objects.all()
    subService = SubService.objects.get(id=id)
    return render(
        request, "service-list.html", {"service": subService, "services": services}
    )
def about(request):
    services = Service.objects.all()
    return render(request, "about.html", {"services": services, 'team': Director.objects.all(), 'testi': Testimonial.objects.all()})
def pricing(request):
    services = Service.objects.all()
    return render(request, "pricing.html", {"services": services})
def service(request):
    services = Service.objects.all()
    return render(request, "service.html", {"services": services})
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if not name or not email or not message:
            return redirect("/contact")
        if not Email.objects.filter(email=email).exists():
            Email.objects.create(email=email)
        Contact.objects.create(name=name, email=email, message=message)
        return JsonResponse({"status": True, 'status': 200}, status=200)
    services = Service.objects.all()
    return render(request, "contact.html", {"services": services})


def project(request):
    services = Service.objects.all()
    return render(request, "project.html", {"services": services})
