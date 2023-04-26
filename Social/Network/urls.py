from django.urls import path
from .views import loginView, registerView, bodyView, logoutView, historyView, deleteView
from . import views
urlpatterns = [
    # Authentication
    path('login/', loginView.as_view(), name='login'),
    path('register/', registerView.as_view(), name='register'),
    path('logout/', logoutView.as_view(), name='logout'),

    # body
    path('body/', bodyView.as_view(), name='body'),
    path('history/', historyView.as_view(), name='history'),
    path('delete/<int:id>/', deleteView.as_view(), name='delete')
]