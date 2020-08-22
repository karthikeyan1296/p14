from django.urls import path
from rsk import views
app_name="rsk"

urlpatterns = [
    path('base/',views.base,name="base"),
    path('home/',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multi/',views.multi,name="multi"),
    path('img/',views.img,name="img"),

]