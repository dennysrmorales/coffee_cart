from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_item/<name>', views.delete_item, name='delete_item'),
    path('add_drink/', views.add_drink, name='add_drink'),
    path('add_snack/', views.add_snack, name='add_snack'),
    path('edit_item/<name>', views.edit_item, name='edit_item'),
    path('features/<name>', views.features, name='features'),
    path('items/<type>', views.items, name='items')

]

