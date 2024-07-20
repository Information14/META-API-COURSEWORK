from django.urls import path 
from . import views

urlpatterns = [
    path('category/', views.Listcategory.as_view()), 
    path('category/<int:pk>', views.Retrievecategory.as_view()),

    path('menuitem/', views.Listmenuitem.as_view()), 
    path('menuitem/<int:pk>', views.Retrievemenuitem.as_view()),
    
    path('cart/', views.Listcart.as_view()),

    path('order/', views.Listorder.as_view()),
    path('order/<int:pk>', views.Retrieveorder.as_view()),

    path('groups/manager/users', views.GroupViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'}))

]
