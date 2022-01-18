from django.shortcuts import render,redirect
from myapp.models import Contact
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')


def skills(request):
    return render(request,'myapp/skills.html')

def service(request):
    return render(request,'myapp/service.html')



def blog(request):
    return render(request,'myapp/blog.html')

def demo(request):
    return render(request,'myapp/demo.html')



def contact(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Subject = request.POST['Subject']
        Message = request.POST['Message']
        Contact(Name=Name,Email=Email,Subject=Subject,Message=Message).save()
        return redirect('home')
    else:
        return render(request, 'myapp/contact.html')



