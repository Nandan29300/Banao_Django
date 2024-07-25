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
    path('create_blog/', views.create_blog, name='create_blog'),
    path('view_blogs/', views.view_blogs, name='view_blogs'),
    path('logout/', views.logout_user, name='logout'),
    path('blog/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]







