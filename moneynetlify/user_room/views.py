from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from .form import RegisterForm
from .models import Post
from .utils import DataMixin


class Home(DataMixin, TemplateView):
    template_name = "user_room/home.html"
    context_object_name = 'manu'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

'''мини блог'''
class Forum(DataMixin, TemplateView):
    template_name = "user_room/forum.html"
    context_object_name = 'manu'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.all()
        c_def = self.get_user_context(title='Forum', post_list=post)
        context = dict(list(context.items()) + list(c_def.items()))
        return context


"""форма регестрации с видео"""
class Register(DataMixin, View):
    template_name = "registration/register.html"
    context_object_name = 'manu'

    def get(self, request):
        context = {
            "form": RegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, username=username, password=password)
            login(request, user)
            return redirect("home")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


"""оствил на всякий случай такой вариает представления формы регестрации, но он свою роль не выполняет"""
class Reg(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))




class Shop(DataMixin, TemplateView):
    template_name = "user_room/shop.html"
    context_object_name = 'manu'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Forum')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class FeedBack(DataMixin, TemplateView):
    template_name = "user_room/feedback.html"
    context_object_name = 'manu'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Forum')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

