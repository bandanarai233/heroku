from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateform, ProfileUpdateForm
from django.urls import reverse_lazy
from users.models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save(force_insert=False, force_update=False, using=None)
            print('form saved')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. Now you can login. {username}!')
            return redirect('login')
        else:
            messages.error(request, f'Your form is invalid!')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            

    else:
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)




# class PasswordResetView(FormView):
#     model = User
#     form_class = PasswordResetForm
#     template_name = 'users/password_reset.html'
#     success_url = reverse_lazy('password_reset_done')


# class PasswordResetDoneView(FormView):
#     model = User
#     form_class = PasswordResetDoneForm
#     template_name = 'users/password_reset_done.html'








    




