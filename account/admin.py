from django.contrib import admin
from account.models import User, AdminProfile, AgentProfile, CustomerProfile

admin.site.register(User) 
admin.site.register(AdminProfile) 
admin.site.register(AgentProfile) 
admin.site.register(CustomerProfile) 
