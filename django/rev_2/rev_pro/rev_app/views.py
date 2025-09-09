from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import RevAppUsers
from .serializers import USER_SERIALIZER


def greeting(req):
    return HttpResponse("good morning!!")


def all_users(req):
    user_data = RevAppUsers.objects.all()
    serialized_data = USER_SERIALIZER(user_data, many=True)

    print(serialized_data.data)  # now prints actual JSON

    # return JSON response with serialized data
    return JsonResponse({"data": serialized_data.data}, safe=False)
