from django.urls import path
from . import views

# from .views import Home

#? endpoint
urlpatterns = [
    # path("", views.Home.as_view(), name="home"), # ?  class based views render file html in django
    # path("", views.Home, name="home")  # ? function based views endpoint
    # path("", views.Home.as_view(), name="home")  # ? class based views endpoint
    # path("<str:name>/", views.Home.as_view(), name="home") # ?class based views drf get argument in request
    # path("", views.Home.as_view(), name="home")  # ?class based views drf get .query_params in request
     path("", views.Home.as_view(), name="home")  # ?class based views drf post .data in request
    
]
