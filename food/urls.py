from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.DetailClassView.as_view(), name='prod_details'),
    path('add_item/', views.AddClassView.as_view(), name='add_item'),
    path('update_item/<int:pk>/', views.UpdateClassView.as_view(), name='update_item'),
    path('delete_item/<int:pk>/', views.DeleteClassView.as_view(), name='delete_item'),
]