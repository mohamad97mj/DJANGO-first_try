from django.urls import path
from . import views


app_name = 'first_app'
urlpatterns = [
    path('', views.user_view, name='user_view'),
    # path('test', views.test, name='test'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
