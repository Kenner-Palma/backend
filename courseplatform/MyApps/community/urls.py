from django.urls import path
from MyApps.community.views import ForumsList, ForumsDetail

app_name = "clientes"
urlpatterns = [
    path('', ForumsList.as_view()),
    path('<int:pk>', ForumsDetail.as_view()),
]