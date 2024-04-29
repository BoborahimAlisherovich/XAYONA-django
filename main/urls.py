from django.urls import path
from .views import home_view, about_view,services_view,blog_view

urlpatterns = [
    path('', home_view, name="home-page"),
    path('about/', about_view, name="about-page"),
    path('blog/', blog_view, name="blog-page"),
    path('services/', services_view, name="services-page"),
]
