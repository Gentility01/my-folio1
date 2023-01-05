from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from user.forms import CreateUserForms

from django.views.generic import CreateView, View
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         user_form = CreateUserForms(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('blogs')
#     else:
#         user_form = CreateUserForms()
    
#     context = {
#         'user_form':user_form
#     }

#     return render(request, "user/register.html", context)

class SignupView(CreateView):
    template_name = "user/register.html"
    success_url = reverse_lazy("signin")
    # context_object_name = "user_form"
    form_class = CreateUserForms

   

