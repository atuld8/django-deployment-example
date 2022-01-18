from django.urls import path
from basic_app import views

# Below is important from the django url templates project point of view
# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('', views.base, name='base'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
