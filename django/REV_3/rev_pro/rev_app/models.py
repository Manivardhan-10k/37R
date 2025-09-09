from django.db import models


# ---------------- Existing Table (Cloned) ----------------
class RevAppUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_mobile = models.CharField(unique=True, max_length=10)
    user_email = models.CharField(unique=True, max_length=50)
    user_password = models.CharField(max_length=255)

    class Meta:
        managed = False   # ✅ since table already exists in DB
        db_table = 'rev_app_users'

    def __str__(self):
        return self.user_name


# ---------------- New Tables (Django-managed) ----------------
class Dept(models.Model):
    id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "dept"

    def __str__(self):
        return self.dept_name


class Emp(models.Model):
    id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=20, null=False)
    emp_dept = models.ForeignKey(
        Dept,
        on_delete=models.CASCADE,
        related_name="employees"
    )

    class Meta:
        db_table = "emp"

    def __str__(self):
        return f"{self.emp_name} ({self.emp_dept.dept_name})"
