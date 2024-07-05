from django.urls import path
from . import views

# from .views import Home


urlpatterns = [
    # path("", views.Home.as_view(), name="home"), # ?  class based views render file html in django
    # path("", views.Home, name="home")  # ? function based views endpoint
    # path("", views.Home.as_view(), name="home")  # ? class based views endpoint
]
