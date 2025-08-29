from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


# -------------------------------
# Custom User Manager
# -------------------------------
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role="USER", **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # keep for Django superusers (developers, not app admins)
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# -------------------------------
# Custom User Model (Email Login)
# -------------------------------
class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"   # app-level admin
        AGENT = "AGENT", "Agent"
        USER = "USER", "User"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.USER)

    # for Django admin site access only
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"

    @property
    def is_admin(self):
        """Business-level admin check"""
        return self.role == self.Roles.ADMIN


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Admin: {self.full_name}"


class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agent_profile")
    agency_name = models.CharField(max_length=150)
    license_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Agent: {self.agency_name}"


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Customer: {self.full_name}"
