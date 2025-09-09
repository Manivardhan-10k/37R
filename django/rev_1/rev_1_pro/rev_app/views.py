from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

##  FBV , CBV


# products={
    
#     "1":"HP laptop",
#     "2":"samsung mobile",
#     "3":"boat headphones"
# }

def welcome(request):
   ## http 
   ##json  
    return JsonResponse({ "response":"welcome to home page!!"})



# def get_product(req,id):
#     if str(id) in products.keys(): 
#         return HttpResponse(products[str(id)])
#     else:
#         return HttpResponse("no product available!!") 
    
    
