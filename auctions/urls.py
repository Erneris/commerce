from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<str:name>", views.listing, name=""),
    path("listings", views.index, name=""),
    path("watchlistadd/<str:name>", views.wladd, name=""),
    path("watchlist", views.wl, name="")
]
