from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    if request.user.is_authenticated == True:
        return render(request, 'homepage.html')
    else:
        return redirect('login')
        