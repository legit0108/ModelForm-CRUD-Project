from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def addAndShow(request):
    if request.method == 'POST':
      form = StudentRegistration(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        user = User(name=name, email=email)
        user.save()
        form = StudentRegistration() # to show blank form post submit
        # form.save() can also use this, no need to instantiate User
    else:
      form = StudentRegistration()      
      users = User.objects.all()
    return render(request, 'enroll/addAndShow.html', {'form': form, 'users': users})
