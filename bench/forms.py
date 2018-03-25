from django import forms
from .models import Company,Country,Currency,Category,Rating,CurrencyName

# class NameForm(forms.ModelForm):

# 	class Meta:
# 		model =  UserDetails
#         fields = ['your_name']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name','title','description','category','video_file']


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['country_name','country_code']

class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ['currency_name','currency_code']

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['ico_profile','team','vision','product']

class CurrencyNameForm(forms.ModelForm):

    class Meta:
        model = CurrencyName
        fields = ['token_name','price','platform','accepting','minimum_investment','soft_cap','hard_cap','country','restricted_areas','bonus','bounty','Whitelist_KYC']

