from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [

    # Tableau de bord
    path("Actualité/", views.tableau_de_bord, name="admin_tableaudebord"),

]