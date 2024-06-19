from django.urls import path
from . import views

app_name = "alpha"
urlpatterns = [
    path("", views.home, name="home"),
    path("product/", views.product, name="product"),
    path("document/", views.document, name="document"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),  # 用户信息页面路由
    path('delete_account/', views.delete_account, name='delete_account'),
]

