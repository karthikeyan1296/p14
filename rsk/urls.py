from django.urls import path
from rsk import views
app_name="rsk"

urlpatterns = [
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),

]