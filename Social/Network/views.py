from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views import View
from .models import Post
from .forms import PostAddForm
# Create your views here.

class loginView(View):
    def get(self, request):
        return render(request, 'user/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('body')
        return render(request, 'user/login.html')

class registerView(View):
        def get(self, request):
            return render(request, 'user/register.html')
        def post(self, request):
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = User.objects.create_user(email=email ,username=username, password=password)
            return redirect('login')

class logoutView(View):
     def get(self, request):
          logout(request)
          return redirect('login')

class bodyView(View):
     def get(self, request):
          user = User.objects.get(username = request.user)
          post_add = PostAddForm()
          context = {'data': user, 'form': post_add}
          return render(request, 'body/body.html', context)
     def post(self, request):
          post = Post()
          post_add = PostAddForm()
          post.caption = request.POST.get('caption')
          post.image = request.FILES.get('image')
          post.user = request.user
          post.save()
          return redirect('history')
     
class historyView(View):
     def get(self, request):
          user = User.objects.get(username = request.user)
          post = Post.objects.all()
          context = {'data': user, 'post':post}
          return render(request, 'body/history.html', context)
     def post(self, request):
          return render(request, 'body/history.html')

class deleteView(View):
     def get(self, request, id):
          post = Post.objects.get(id = id)
          post.delete()
          return redirect('history')
