import json
from django.shortcuts import render
from django.views import View
from django import forms
import redis
from .form import userForm
from django.shortcuts import redirect

r = redis.Redis(
  host='redis-17833.c281.us-east-1-2.ec2.cloud.redislabs.com',
  port=17833,
  password='pVIA3FAUubQVvloelCR86fHJlGcv3Eux')  


def my_view(request):
    form = userForm()  # Create an instance of your form
    return render(request, "test.html", {"form": form})

from .form import userForm
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charities/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charities/about.html')
    
def getUser(request):
    if request.method == "POST":
        form = userForm(request.POST)
        data = form.data     
        user = {
            "companyname": data["company_name"],
            "fulladdress": data["location"],
            "weight": data["weight"],
            "food_category": data["food_category"],
            "quantity": data["quantity"],
            "weightperitem": data["weight_per_item"],
            "valueperitem": data["value_per_item"],
            "email": data["email"]


        }
    

        r.lpush("happy times", json.dumps(user))
        # create the user object from the form
        # store the user into redis, using an id for the key
        # redirect to pzge with users
    else:
        form = userForm()

    return render(request, "charities/form.html", {"form": form})
        

def getTest(request):
    users = r.lrange("happy times", 0, -1)
    #happy_dict = json.loads(happy)
    ls = []
    for user in users:
        i = json.loads(user)
        ls.append(i)


    return render(request, "charities/test.html", {"test": ls})

