from django.urls import path

from . import views


# urlpatterns = [

# path("api/", views.ListProfile, name="ListProfile"),
# path(
#     "api/<id>/",
#     views.update_and_delete_UserProfile,
#     name="update_and_delete_UserProfile",
# ),
# ]


urlpatterns = [
    path("api/", views.UserProfileView.as_view(), name="UserProfileView"),
    path(
        "api/<int:id>/", views.UserProfileView.as_view(), name="UserProfileDetailView"
    ),
]
