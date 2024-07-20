# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('dashboard/', views.dashboard, name='dashboard'),
# ]

# urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login_view, name='login_view'),  # Ensure this matches the view function name
#     path('dashboard/', views.dashboard, name='dashboard'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]







