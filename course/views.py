from django.shortcuts import render
from . models import Course
# Create your views here.
def webdevelopment(request):
    courses = Course.objects.all()

    return render(request, 'webdevelopment.html', {'is_webdevelopment_page': True, 'courses': courses})

