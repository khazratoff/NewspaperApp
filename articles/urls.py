from django.urls import path
from . import views


urlpatterns = [
    path('',views.ArticlesListView.as_view(), name = 'articles'),
    path('detailed/<int:pk>',views.ArticlesDetailView.as_view(), name = 'detail-article'),
    path('create/',views.ArticlesCreateView.as_view(), name = 'create-article'),
    path('update/<int:pk>/', views.ArticlesUpdateView.as_view(), name = 'update-article'),
    path('delete/<int:pk>/',views.ArticlesDeleteView.as_view(), name = 'delete-article'),

]