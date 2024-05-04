from django.forms import ModelForm
from food.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"