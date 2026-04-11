from django.urls import path
from . import views


app_name = "store"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("product/",views.product,name="product"),
    path("detail_post/<str:detail>",views.detail,name="detail"),
    path("about/",views.about,name="about"),
    path("con/",views.con,name="con"),
    path("con/<str:price>",views.con,name="con_with_subject"),
]
