from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import customer
import json
# Create your views here.
@csrf_exempt
def api_data(request):
    if request.method == 'POST':
        print("hii")
        # Load JSON data from request body
        data = json.loads(request.body)
        print(data)
        # Extract username and password from flutter JSON data
        f_uname = data.get('username', None)
        f_pwd = data.get('password', None)
        print(f_uname)
        print(f_pwd)
        details = {
            'user': f_uname,
            'pass': f_pwd
        }
        return JsonResponse({'data': details}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def index(request):
    return render(request, "index.html")
