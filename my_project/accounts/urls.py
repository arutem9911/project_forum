from django.urls import path
from accounts import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users/<int:id>/detail/', views.UserDetailView.as_view(), name='detail_user'),
]
