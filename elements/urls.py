from django.urls import path
from . import views

app_name='elements'
urlpatterns = [
    path('add', views.add, name='add'),
 
]

"""path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('', views.index, name='index')"""