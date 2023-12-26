from django import forms
from .models import ImageProduct, Product, Color, Size

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ImageForm(forms.ModelForm):
    image = MultipleFileField()
    class Meta:
        model = ImageProduct
        fields = ('image', )
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'sub_category', 'name', 'avatar', 'size', 'color', 'price', 'price_original', 'descrip', 'status', 'quantity_remain')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.fields['category'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['sub_category'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = 'form-control'
        self.fields['size'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price_original'].widget.attrs['class'] = 'form-control'
        self.fields['descrip'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['quantity_remain'].widget.attrs['class'] = 'form-control'
        

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.fields['color'].widget.attrs['class'] = 'form-control'  
        

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.fields['size'].widget.attrs['class'] = 'form-control'  
