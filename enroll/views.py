from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# add new items, show all items
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

# update
def update_data(request, id):
  if request.method == 'POST':
    user = User.objects.get(pk=id)
    form = StudentRegistration(request.POST, instance=user)
    if form.is_valid():
      form.save()
  else:
    user = User.objects.get(pk=id)
    form = StudentRegistration(instance=user)
  return render(request, 'enroll/updatestudent.html', {'form': form})
# delete
def delete_data(request, id):
  if request.method == 'POST':
    user = User.objects.get(pk=id)  
    user.delete()
    return HttpResponseRedirect('/')