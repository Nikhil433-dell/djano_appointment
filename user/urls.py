from django import views
from django.urls import path
from user import views


urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logout, name="logout"),
    path('home/<int:id>', views.home, name="home"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('bookap/<int:id>', views.bookap, name="bookap"),
    path('doctors/<int:id>', views.doctors, name="doctors"),
    path('confirmap/<int:id>', views.confirmap, name="confirmap"),
    path('create_blog/<int:id>', views.create_blog, name="create_blog"),
    path('user_details/<int:id>', views.user_details, name="user_details"),
    path('drafted_blog/<int:id>', views.drafted_blog, name="drafted_blog"),
    path('blog_details/<int:id>', views.blog_details, name="blog_details"),
]