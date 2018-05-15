from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Drinks,Snacks
from .forms import ItemForm

def index(request):
	snacks_list = Snacks.objects.order_by('id')
	drinks_list = Drinks.objects.order_by('id')
	context = {'snacks_list': snacks_list, 'drinks_list': drinks_list}

	return render(request, 'cart/index.html', context)

def items(request, type):
	if type == 'snack':
		items_list = Snacks.objects.order_by('id')
		url = 'cart/scone.png'

	elif type =='drink':
		items_list = Drinks.objects.order_by('id')
		url = 'cart/drink_2.png'

	context = {'items_list': items_list, 'url': url }
		
	return render(request, 'cart/items.html', context)

def delete_item(request, name):
	if Drinks.objects.filter(name=name).count() == 1:
		item = Drinks.objects.get(name=name)

	elif Snacks.objects.filter(name=name).count() == 1:
		item = Snacks.objects.get(name=name)

	item.delete()
	return redirect('index')

def add_drink(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)

		if Drinks.objects.filter(name=request.POST['name']).count() == 1:
			drink = Drinks.objects.get(name=request.POST['name'])
			ing = request.POST['ingredients']
			rec = request.POST['recommendations']

			drink.ingredients = ing
			drink.recommendations = rec
			drink.save()
			return redirect('index')

		else:

			if form.is_valid():
				new_item = Drinks(name=request.POST['name'], ingredients=request.POST['ingredients'], recommendations=request.POST['recommendations'])
				new_item.save()
				return redirect('index')

	else:
		form = ItemForm()

	context = {'form': form, 'action': 'Add', 'button_action': 'Add'}
	return render(request, 'cart/add_drink.html', context)

def edit_item(request, name):
	if Drinks.objects.filter(name=name).count() == 1:
		item = Drinks.objects.get(name=name)
		url = 'cart/add_drink.html'

	elif Snacks.objects.filter(name=name).count() == 1:
		item = Snacks.objects.get(name=name)
		url = 'cart/add_snack.html'

	name = item.name
	ingredients = item.ingredients
	recs = item.recommendations

	form = ItemForm(initial={"name":name, "ingredients": ingredients, "recommendations": recs })
	context = {'form': form, 'action': 'Edit', 'button_action': 'Save'}

	return render(request, url, context)

def add_snack(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)

		if Snacks.objects.filter(name=request.POST['name']).count() == 1:
			snack = Snacks.objects.get(name=request.POST['name'])
			ing = request.POST['ingredients']
			rec = request.POST['recommendations']

			snack.ingredients = ing
			snack.recommendations = rec
			snack.save()
			return redirect('index')

		else:

			if form.is_valid():
				new_item = Snacks(name=request.POST['name'], ingredients=request.POST['ingredients'], recommendations=request.POST['recommendations'])
				new_item.save()
				return redirect('index')

	else:
		form = ItemForm()

	context = {'form': form, 'action': 'Add', 'button_action': 'Add'}
	return render(request, 'cart/add_snack.html', context)

def features(request, name):
	if Drinks.objects.filter(name=name).count() == 1:
		item = Drinks.objects.get(name=name)
		url = 'cart/drink_2.png' 

	elif Snacks.objects.filter(name=name).count() == 1:
		item = Snacks.objects.get(name=name)
		url = 'cart/scone.png'

	context = {'item': item, 'url': url}
	return render(request, 'cart/features.html', context)


