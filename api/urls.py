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
    path("api/list/", views.ListUserProfileView.as_view(), name="listUserProfile"),
    path(
        "api/create/", views.CreateUserProfileView.as_view(), name="CreateUserProfile"
    ),
    path(
        "api/list-create/",
        views.ListCreateUserProfileView.as_view(),
        name="ListCreateUserProfile",
    ),
]
