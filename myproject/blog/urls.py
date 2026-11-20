from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # path('about',views.about),
    path('addpost',views.addpost , name="addpost"),
]
