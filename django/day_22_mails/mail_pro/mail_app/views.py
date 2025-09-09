from django.shortcuts import render

import json
from django.http import HttpResponse, JsonResponse

from django.core.mail import send_mail,EmailMessage

# Create your views here.


def register(req):
    user_data=json.loads(req.body) 
    if user_data["email"]:
        # send_mail(
        #     subject="WELCOME MAIL",
        #     message=f"Welcome to the APP  {user_data['name']}!!",
        #     from_email="manivardhan.10kcoders@gmail.com",
        #     recipient_list=[user_data["email"]],
        #     fail_silently=False,
        # )
        
        email=EmailMessage(
            subject="WELCOME MAIL with attachement",
            body=f"Welcome to the APP  {user_data['name']}!! , check the attachment below!!",
            from_email="manivardhan.10kcoders@gmail.com",
            to=[user_data["email"]]    
        )
        email.attach_file("C:\\Users\makam\Downloads\Django_Email_Guide_Updated.docx")
        email.send()
        return JsonResponse({"msg":"mail sent successfully!!"})
    return HttpResponse("data recieved!")
    # user_name=
    
    
    