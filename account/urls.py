from django.urls import path
from account.views import userlogin, signup, forgot_password, dashboard, profile, usersettings, users, reports, logout

urlpatterns = [
    # path('login/', userlogin, name="login"),
    path('signup/', signup, name="register"),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('settings/', usersettings, name="settings"),
    path('users/', users, name="users"),
    path('reports/', reports, name="reports"),
    path('logout/', logout, name="logout"),
]
