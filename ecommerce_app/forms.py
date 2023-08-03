from django import forms


class shopform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)


class userform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)

class shoploginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)

class userloginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)

class addproductform(forms.Form):
    name=forms.CharField(max_length=30)
    proid=forms.IntegerField()
    image=forms.ImageField()
    price=forms.IntegerField()
    description=forms.CharField(max_length=200)

class contactusform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    message=forms.CharField(max_length=200)

