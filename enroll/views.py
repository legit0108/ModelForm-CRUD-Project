from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def addAndShow(request):
    if request.method == 'POST':
      form = StudentRegistration(request.POST)
    else:
      form = StudentRegistration()      
      return render(request, 'enroll/addAndShow.html', {'form': form})
