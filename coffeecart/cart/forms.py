from django import forms

class ItemForm(forms.Form):
	name = forms.CharField(max_length=40, 
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}))

	ingredients = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ex: ["Milk", "Sugar", "Eggs"]'}))
	recommendations = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ex: ["Muffin", "Cookie"]'}))