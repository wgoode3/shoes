from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('shoes', views.shoes),
    path('logout', views.logout),
    path('dashboard/<int:user_id>', views.dashboard),
    path('sell_shoes', views.sell_shoes),
    path('buy_shoes/<int:shoe_id>', views.buy_shoes),
    path('remove/<int:shoe_id>', views.remove)
]