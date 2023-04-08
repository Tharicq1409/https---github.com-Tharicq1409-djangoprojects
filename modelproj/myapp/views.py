from django.shortcuts import render
from myapp.models import Person
# Create your views here.
def user_details(request):
    person =Person.objects.all()
    context={'person':person}
    return render(request,'index.html',context)