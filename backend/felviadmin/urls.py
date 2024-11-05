from django.urls import path
from . import views


urlpatterns = [
    path('felviadmin/', views.index, name='index'),
    path('ujadat/', views.ujAdatWeblap, name="ujadat"),
    path('ujadat_form/', views.ujAdatForm, name="ujadat_form"),
    path('ujadatrogzit/', views.ujAdatRogzit, name="ujadatrogzit"),
    path('torles/<int:itemId>', views.torolAdat, name="torles"),
    path('modositas/<int:itemId>', views.modositAdat, name="modositas"),
    path('modositrogzit/', views.modositRogzit, name="modositasrogzit"),
    path('ujszak/', views.ujSzakWeblap, name="ujszak"),
    path('ujszak_form/', views.ujSzakForm, name="ujszak_form"),
    path('ujszakrogzit/', views.ujSzakRogzit, name="ujszakrogzit"),
    path('feladat/', views.feladat_views, name="feladat_name"),
]