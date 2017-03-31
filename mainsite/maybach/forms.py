from .models import Category, Product
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category',)

    def __init__(self, user, *args,**kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
