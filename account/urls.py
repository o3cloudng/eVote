from django.urls import path
from account.views import userlogin, signup, forgot_password, dashboard, profile, \
        usersettings, users, reports, logout, budget, payment_register

urlpatterns = [
    # path('login/', userlogin, name="login"),
    path('signup/', signup, name="signup"),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('profile/', profile, name="profile"),
    path('settings/', usersettings, name="settings"),
    path('users/', users, name="users"),
    path('reports/', reports, name="reports"),
    path('logout/', logout, name="logout"),
    path('budget/', budget, name="budget"),
    path('payment_register/', payment_register, name="payment_register"),
]
