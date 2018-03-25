# -*- coding: utf-8 -*-
import json
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth as django_auth
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseBadRequest,HttpResponse
from django.shortcuts import get_object_or_404
from .models import Company,Country,Currency,Category,Rating,CurrencyName
from .forms import CompanyForm,CountryForm,CurrencyForm,CategoryForm,RatingForm,CurrencyNameForm,LoginForm

# Create your views here.

def login(request, template="accountLogin.html", context={}):
    next_url = request.GET.get('next', False)
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = django_auth.authenticate(username=username, password=password)
            print user
            if user is not None:
                if user.is_active:
                    django_auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, _('You have successfully logged in.'))
                    if next_url:
                        return redirect(next_url)
                    else:
                        return redirect(reverse('company_list'))
                else:
                    messages.add_message(request, messages.WARNING, _('Non active user.'))
            else:
                messages.add_message(request, messages.ERROR, _('Wrong username or password.'))

    context['form'] = login_form
    return render(request, template, context)

def company_list(request):
	companies = Company.objects.all()
	return render(request, 'company_list.html',{'companies': companies,})

def company_add(request):
	if request.method == 'POST':
		form = CompanyForm(request.POST, None)
		print "--------------",form
		if form.is_valid():
			company = form.save(commit=False)
			form.save()
			company.save()
			return redirect('company_list')
		else:
			error_dict = {}
			for error in form.errors:
				error_dict[error] = form.errors[ error]

			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CompanyForm()
		return render(request, 'company_add.html', {'form':form})


def company_detail(request, id):
	company = get_object_or_404(Company, id=id)
	print company.category.all()
	return render(request, 'company_detail.html', {
		       	"company":company,
						})



def company_edit(request,id):
	company = get_object_or_404(Company, id=id)
	if request.method == "POST":
		form = CompanyForm(request.POST, instance=company)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
			return HttpResponse('ok ')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error] = form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CompanyForm(instance=company)
	return render(request, 'company_edit.html', {'form': form ,'is_edit_mode':True,'id':id})


def company_delete(request,id):
	companies = Company.objects.get(id=id)
	companies.delete()
	return HttpResponse('ok ')


def country_add(request):
	if request.method=='POST':
		form=CountryForm(request.POST,None)
		print "--------",form
		if form.is_valid():
			country=form.save(commit=False)
			form.save()
			country.save()
			return redirect('index')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error]=form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form=CountryForm()
	return render(request,'country_add.html',{'form':form})

def country_edit(request,id):
	country = get_object_or_404(Country,id=id)
	if request.method == 'POST':
		form = CountryForm(request.POST,instance=country)
		if form.is_valid():
			country = form.save(commit=False)
			country.save()
			return HttpResponse('ok')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error] = form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CountryForm(instance=country)
	return render(request, 'country_edit.html', {'form': form ,'is_edit_mode':True,'id':id})


def country_list(request):
	countries = Country.objects.all()
	return render(request,'country_list.html',{'countries':countries,})

def country_delete(request,id):
	countries = Country.objects.get(id=id)
	countries.delete()
	return HttpResponse('ok')

def currency_add(request):
	if request.method == 'POST':
		form = CurrencyForm(request.POST, None)
		print "--------------",form
		if form.is_valid():
			currency = form.save(commit=False)
			form.save()
			currency.save()
			return redirect('index')
		else:
			error_dict = {}
			for error in form.errors:
				error_dict[error] = form.errors[ error]

			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CurrencyForm()
		return render(request, 'currency_add.html', {'form':form})

def currency_edit(request,id):
	currency = get_object_or_404(Currency, id=id)
	if request.method == "POST":
		form = CurrencyForm(request.POST, instance=currency)
		if form.is_valid():
			currency = form.save(commit=False)
			currency.save()
			return HttpResponse('ok ')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error] = form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CurrencyForm(instance=currency)
	return render(request, 'currency_edit.html', {'form': form ,'is_edit_mode':True,'id':id})

def currency_list(request):
	currencies = Currency.objects.all()
	return render(request,'currency_list.html',{'currencies':currencies,})

def currency_delete(request,id):
	currencies = currency.objects.get(id=id)
	currencies.delete()
	return HttpResponse('ok')

def category_add(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST, None)
		print "--------------",form
		if form.is_valid():
			category = form.save(commit=False)
			form.save()
			category.save()
			return redirect('index')
		else:
			error_dict = {}
			for error in form.errors:
				error_dict[error] = form.errors[ error]

			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CategoryForm()
		return render(request, 'category_add.html', {'form':form})

def category_edit(request,id):
	category = get_object_or_404(Category, id=id)
	if request.method == "POST":
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			category = form.save(commit=False)
			category.save()
			return HttpResponse('ok ')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error] = form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CategoryForm(instance=category)
	return render(request, 'category_edit.html', {'form': form ,'is_edit_mode':True,'id':id})

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'category_list.html',{'categories': categories,})

def category_delete(request,id):
	categories = Category.objects.get(id=id)
	categories.delete()
	return HttpResponse('ok ')

def rating_add(request):
	if request.method == 'POST':
		form = RatingForm(request.POST, None)
		print "--------------",form
		if form.is_valid():
			rating = form.save(commit=False)
			form.save()
			rating.save()
			return redirect('index')
		else:
			error_dict = {}
			for error in form.errors:
				error_dict[error] = form.errors[ error]

			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = RatingForm()
		return render(request, 'rating_add.html', {'form':form})

def rating_edit(request,id):
	rating = get_object_or_404(Rating, id=id)
	if request.method == "POST":
		form = RatingForm(request.POST, instance=rating)
		if form.is_valid():
			rating = form.save(commit=False)
			rating.save()
			return HttpResponse('ok ')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error] = form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = RatingForm(instance=rating)
	return render(request, 'rating_edit.html', {'form': form ,'is_edit_mode':True,'id':id})

def rating_list(request):
	ratings = Rating.objects.all()
	return render(request, 'rating_list.html',{'ratings': ratings,})

def rating_delete(request,id):
	ratings = Rating.objects.get(id=id)
	ratings.delete()
	return HttpResponse('ok ')

def currencyname_add(request):
	if request.method == 'POST':
		form = CurrencyNameForm(request.POST, None)
		print "--------------",form
		if form.is_valid():
			currencyname = form.save(commit=False)
			form.save()
			currencyname.save()
			return redirect('index')
		else:
			error_dict = {}
			for error in form.errors:
				error_dict[error] = form.errors[ error]

			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CurrencyNameForm()
		return render(request, 'currencyname_add.html', {'form':form})

def currencyname_edit(request,id):
	currencyname = get_object_or_404(CurrencyName, id=id)
	if request.method == "POST":
		form = CurrencyNameForm(request.POST, instance=currencyname)
		if form.is_valid():
			currencyname = form.save(commit=False)
			currencyname.save()
			return HttpResponse('ok ')
		else:
			error_dict={}
			for error in form.errors:
				error_dict[error] = form.errors[error]
			return HttpResponseBadRequest(json.dumps(error_dict))
	else:
		form = CurrencyNameForm(instance=currencyname)
	return render(request, 'currencyname_edit.html', {'form': form ,'is_edit_mode':True,'id':id})

def currencyname_list(request):
	currenciesname = CurrencyName.objects.all()
	return render(request, 'currencyname_list.html',{'currenciesname': currenciesname,})

def currencyname_delete(request,id):
	currenciesname = CurrencyName.objects.get(id=id)
	currenciesname.delete()
	return HttpResponse('ok ')

	
def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/formvalidate/')
	else:
		form = NameForm()
		return render(request,'formvalidate.html',{'form':form})


def company_add_ajax(request):
	data = { }
	if request.is_ajax():
		print request
		data['a'] = 'a'
		data['b'] = 'b'

		return HttpResponse('Succesfully created client')
		return HttpResponse(json.dumps(data))


def country_add_ajax(request):
	data = { }
	if request.is_ajax():
		print request
		data['a'] = 'a'
		data['b'] = 'b'

		return HttpResponse('Succesfully created client')
		return HttpResponse(json.dumps(data))

def currency_add_ajax(request):
	data = { }
	if request.is_ajax():
		print request
		data['a'] = 'a'
		data['b'] = 'b'

		return HttpResponse('Succesfully created client')
		return HttpResponse(json.dumps(data))

def category_add_ajax(request):
	data = { }
	if request.is_ajax():
		print request
		data['a'] = 'a'
		data['b'] = 'b'

		return HttpResponse('Succesfully created client')
		return HttpResponse(json.dumps(data))

def rating_add_ajax(request):
	data = { }
	if request.is_ajax():
		print request
		data['a'] = 'a'
		data['b'] = 'b'

		return HttpResponse('Succesfully created client')
		return HttpResponse(json.dumps(data))

def currencyname_add_ajax(request):
	data = { }
	if request.is_ajax():
		print request
		data['a'] = 'a'
		data['b'] = 'b'

		return HttpResponse('Succesfully created client')
		return HttpResponse(json.dumps(data))