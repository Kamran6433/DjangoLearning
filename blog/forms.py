from django import forms

# Link to django forms fields: https://docs.djangoproject.com/en/4.2/ref/forms/fields/

class CreateAccount(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    age = forms.IntegerField(label="Age")
    email = forms.EmailField(label="Email")
    password = forms.PasswordInput()
    