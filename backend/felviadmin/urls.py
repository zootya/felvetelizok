from django.urls import path
from . import views

app_name = "felviadmin"
urlpatterns = [
    path('felviadmin/', views.index, name='index'),
    path('ujadat/', views.ujAdatWeblap),
    path('ujadatrogzit/', views.ujAdatRogzit),
    path('torles/<int:itemId>', views.torolAdat),
    path('ujszak/', views.ujSzakWeblap),
    path('ujszakrogzit/', views.ujSzakRogzit),
]