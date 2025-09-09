from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import RevAppUsers, Dept, Emp
from .serializers import user_serializer


def sample(request):
    return HttpResponse("API working ✅")


# ---------------- RevAppUsers ----------------
def all_users(request):
    users = RevAppUsers.objects.all()
    serialized_data = user_serializer(users, many=True)
    return JsonResponse({"all_users": serialized_data.data})


def get_user(request, id):
    user = get_object_or_404(RevAppUsers, id=id)
    serialized_data = user_serializer(user)
    return JsonResponse({"user_data": serialized_data.data})


# ---------------- Dept & Emp ----------------
def all_departments(request):
    data = Dept.objects.all().values("id", "dept_name")
    return JsonResponse({"departments": list(data)})


def all_employees(request):
    data = Emp.objects.select_related("emp_dept").values(
        "id", "emp_name", "emp_dept__dept_name"
    )
    return JsonResponse({"employees": list(data)})


def employees_by_department(request, dept_id):
    dept = get_object_or_404(Dept, id=dept_id)
    employees = dept.employees.all().values("id", "emp_name")
    return JsonResponse({
        "department": dept.dept_name,
        "employees": list(employees)
    })


def delete_department(request, dept_id):
    dept = get_object_or_404(Dept, id=dept_id)
    dept.delete()  # ✅ CASCADE will delete employees too
    return JsonResponse({"msg": f"Department {dept.dept_name} deleted with its employees"})
