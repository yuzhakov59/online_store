from django import forms
from django.core.exceptions import ValidationError


from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'picture', 'category', 'price', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название продукта'  # Текст подсказки внутри поля
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Описание'  # Текст подсказки внутри поля
        })

        self.fields['picture'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Картинка'  # Текст подсказки внутри поля
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену'  # Текст подсказки внутри поля
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'type': 'data'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'type': 'data'
        })


    def clean_name(self):
        name = self.cleaned_data.get('name')
        banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        name_lower = name.lower()

        for word in banned_words:
            if word in name_lower:
                raise ValidationError('Наименование не должно содержать запрещенных слов')
        return name


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price
