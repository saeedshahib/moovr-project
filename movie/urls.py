from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    # path('', views.all_blogs, name='all_blogs'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/comment', views.AddComment, name='AddComment'),
]
