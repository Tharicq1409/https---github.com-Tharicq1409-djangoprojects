from django.shortcuts import render
from .models import Employee

# Create your views here.
'''
def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'index.html', context)'''


def employee_list(request):
    query = request.GET.get('qu')
    if query:
        employees = Employee.objects.filter(name__icontains=query)
        context = {'employees': employees, 'query': query}
        return render(request, 'details.html', context)
    else:
        return render(request, 'index.html')
        #employees = Employee.objects.all()



