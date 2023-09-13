from django.shortcuts import render, redirect
from user_auth.models import User

# Create your views here.
def index(request):
    if request.session.has_key('user_id'):
        return render(request, 'index.html')
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'Incorrect Password'})
        except:
            return render(request, 'login.html', {'error': 'Invalid Username'})
    return render(request, 'login.html')

def logout(request):
    del request.session['user_id']
    return redirect('login')