

from django import forms
import redis

class userForm(forms.Form):
    company_name = forms.CharField(label="Company Name", max_length = 100)
    location = forms.CharField(label="Full Address (Streetname, Postal Code)", max_length = 100)
    email = forms.CharField(label="email", max_length = 100)
    weight = forms.CharField(label="Food Weight (Ibs only)", max_length = 100)
    FOOD_CATEGORIES = (
        ('', 'Choose...'),  
        ('Prep', 'Prepared Food'),
        ('Shelf', 'Shelf Stable'),
        ('Raw', 'Raw Ingredients'),

    )
    food_category = forms.ChoiceField(label="Food Category", choices=FOOD_CATEGORIES)
    quantity = forms.CharField(label="Quantity", max_length = 100)
    weight_per_item = forms.CharField(label="Weight Per Item (Ibs only)", max_length = 100)
    value_per_item = forms.CharField(label="Value per item", max_length = 100)


    r = redis.Redis(
  host='redis-17833.c281.us-east-1-2.ec2.cloud.redislabs.com',
  port=17833,
  password='pVIA3FAUubQVvloelCR86fHJlGcv3Eux')    

   
 
    

