from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from userapp.models import UserProfile

@login_required
def view_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        return redirect('view_profile')

    return render(request, 'edit_profile.html', {'profile': profile})
