from django.shortcuts import render
from formsapp.forms import Contactform
# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        user_name = request.POST['name']
        email_id = request.POST['email']
        content = request.POST['content']

        new_user = Contactform(name=user_name,email=email_id,content=content)
        new_user.save()
    return render(request,'formapp/index.html',{'form':form})
'''
        if form.is_valid():
            form.save()
            return render(request, 'formapp/contact.html')
    else:
        form = Contactform(request.POST)
    return render(request, 'formapp/index.html', {'form': form})
'''    
    #con=Contactform()
    #return render(request,'formsapp/index.html',{'form':con})

    