from django.shortcuts import redirect, render
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(redirect_field_name=None)
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect(f'/admin/login/?next=/home')